<template>
  <div>
    <div class="text-center mt-5 mx-5">
      <vs-button size="xl" danger type="filled" @click="goToHome">
        Volver
      </vs-button>
    </div>
    <div class="flex justify-center">
      <ManagementClinicHistory />
    </div>
  </div>
</template>
<script>
import ManagementClinicHistory from "@/components/ClinicHistory/ManagementClinicHistory.vue";
export default {
  components: { ManagementClinicHistory },
  data() {
    return {};
  },
  methods: {
    goToHome() {
      this.$router.push("/");
    },
  },
};
</script>
