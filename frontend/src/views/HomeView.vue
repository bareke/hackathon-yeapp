<template>
  <div class="home flex justify-center items-center">
    <!-- <HelloWorld /> -->
    <ManagementClinicHistory />
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import ManagementClinicHistory from "@/components/ClinicHistory/ManagementClinicHistory.vue";

export default {
  name: "HomeView",
  components: {
    // HelloWorld,
    ManagementClinicHistory,
  },
};
</script>
