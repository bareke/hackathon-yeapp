<template>
  <div class="flex justify-center items-center">
    <!-- <HelloWorld /> -->
    <HomeComponent />
    <router-view></router-view>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import HomeComponent from "@/components/HomeComponent.vue";

export default {
  name: "HomeView",
  components: {
    // HelloWorld,
    HomeComponent,
  },
};
</script>
