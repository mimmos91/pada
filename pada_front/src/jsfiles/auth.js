import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null, // 사용자 정보
  }),
  getters: {
    isAuthenticated: (state) => !!state.user, // 로그인 여부 확인
  },
  actions: {
    async fetchUser() {
      try {
        const response = await axios.get('/api/user', { withCredentials: true })
        this.user = response.data // 사용자 정보 저장
      } catch (error) {
        this.user = null // 인증 실패 시 상태 초기화
        if (error.response && error.response.status === 401) {
          console.error('401 Unauthorized: 인증되지 않은 사용자')
        } else {
          console.error('사용자 상태를 가져오는 중 오류 발생:', error.message)
        }
        throw error // 에러를 다시 던져서 라우터 가드로 전달
      }
    },
    async login(credentials) {
      await axios.get('/sanctum/csrf-cookie') // CSRF 초기화
      const response = await axios.post('/api/login', credentials, { withCredentials: true })
      this.user = response.data.user // 로그인 성공 시 사용자 정보 저장
    },
    async logout() {
      await axios.post('/api/logout', {}, { withCredentials: true })
      this.user = null // 로그아웃 시 상태 초기화
    },
  },
})
