<script setup>
// import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <router-view />
</template>

<style scoped>
header {
  line-height: 1.5;
  width: 100%;
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
    /* place-items: start center; */
    /* flex-wrap: wrap; */
  }
}
</style>
