<!-- <script setup></script> -->

<template>
  로그인
  <div>
    <!-- 공통 AppBar -->
    <div
      class="app-bar bg-blue-500 text-white shadow-md px-4 py-2 flex justify-between items-center"
    >
      <div class="text-xl font-semibold">PADA (Posco Automated Data Analysis) 🧐</div>
      <div class="flex space-x-4">
        <router-link to="/" class="hover:bg-blue-600 rounded px-3 py-1 transition">홈</router-link>
        <router-link
          v-if="!isAuthenticated"
          to="/login"
          class="hover:bg-blue-600 rounded px-3 py-1 transition"
          >로그인</router-link
        >
        <router-link
          v-if="!isAuthenticated"
          to="/register"
          class="hover:bg-blue-600 rounded px-3 py-1 transition"
          >회원가입</router-link
        >
        <button
          v-if="isAuthenticated"
          @click="showLogoutModal"
          class="hover:bg-blue-600 rounded px-3 py-1 transition"
        >
          로그아웃
        </button>
        <router-link
          v-if="isAuthenticated"
          to="/user-info"
          class="hover:bg-blue-600 rounded px-3 py-1 transition"
          >유저정보</router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {}
  },
  methods: {},
  components: {},
}
</script>

<style scoped>
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
    text-align: left;
  }
}
</style>
