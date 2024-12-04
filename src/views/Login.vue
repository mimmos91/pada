<!-- <script setup></script> -->

<template>
  <!-- 공통 AppBar -->
  <div>
    <div style="place-items: center" class="login-container">
      <img src="../assets/logo.png" alt="PADA Logo" />
      <input type="text" v-model="id" placeholder="아이디" />
      <input type="password" v-model="pwd" placeholder="비밀번호" />
      <button>로그인</button>
      <div class="text">
        <p>* 시스템 문의: 광양 도금부 기술개발섹션 박현준 (mechpark@posco.com)</p>
        <p>
          PADA 시스템 사용이 필요하신 경우: 시스템 문의처로 사유와 함께 메일주시면 검토 후
          회신드리겠습니다.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from '@/jsfiles/auth'

export default {
  name: 'Login',
  data() {
    return {
      id: '',
      pwd: '',
    }
  },
  methods: {
    async login() {
      const authStore = useAuthStore()
      try {
        // const response = await axios.post('')
        const submit = async () => {
          await authStore.login({ email: this.id, password: this.pwd })

          if (Response.data.success) {
            this.$router.push({
              name: 'PADA',
              params: { userInfo: Response.data.user },
            })
          } else {
            alert('아이디나 비밀번호를 확인하십시오.')
          }
        }
      } catch (error) {
        console.error(error)
        alert('로그인 중 오류가 발생하였습니다.')
      }
    },
  },
  components: {},
}
</script>

<style scoped>
#app {
  margin: auto;
}
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: center;
  }
}
body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 300vh;
  margin: 30px;
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
}

.login-container {
  width: 400px;
  height: 600px;
  padding: 30px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  text-align: center;
}

.login-container img {
  width: 150px;
  padding-bottom: 30px;
  margin: auto;
}

.login-container input {
  width: 100%;
  padding: 15px;
  margin: 20px 0;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
}

.login-container button {
  width: 100%;
  margin: 20px 0;
  padding: 15px;
  background-color: #c7d4f1;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

.login-container button:hover {
  background-color: #a8bce1;
}

.login-container .text {
  width: 100%;
  margin: 20px 0;
  text-align: start;
  text-size-adjust: unset;
}

.text p {
  padding: 3px;
}
</style>
