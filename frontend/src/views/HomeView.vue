<template>
  <div class="home flex justify-center items-center">
    <!-- <HelloWorld /> -->
    <CreateForm />
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import CreateForm from "@/components/CreateForm.vue";

export default {
  name: "HomeView",
  components: {
    // HelloWorld,
    CreateForm,
  },
};
</script>
