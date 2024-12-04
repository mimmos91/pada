<script setup>
import login from './views/Login.vue'
import HelloWorld from './components/HelloWorld.vue'
// import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <header>
    <!-- <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" /> -->
    <!-- 안녕하세요 아 잘 되고 있었구나
    <div class="wrapper">
      <HelloWorld msg="You did it! HAHA" />
    </div>
    <div>
      <nav>
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/manager">About</router-link></li>
          <li><router-link to="/login">login</router-link></li>
        </ul>
      </nav>

    </div> -->
    <router-view />
  </header>

  <main></main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: block;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper main {
    /* display: block;
     */
    display: block;
    place-items: start center;
    /* flex-wrap: wrap; */
  }
}
</style>
