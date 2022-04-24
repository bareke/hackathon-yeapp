<template>
  <div
    class="shadow-xl w-10/12 mt-5 flex flex-col justify-center gap-4 items-center w-full rounded-xl"
  >
    <div class="w-full">
      <step-progress
        :steps="steps"
        :current-step="currentStep"
        icon-class="fa fa-check"
        active-color="blue"
      ></step-progress>
    </div>
    <h1 v-if="currentStep === 0" class="text-4xl mb-4">
      Registrar nueva historia clinica
    </h1>
    <FormUserInfo v-if="currentStep === 1" />
    <ConsultReason v-if="currentStep === 2" />

    <div class="flex gap-5">
      <vs-button type="filled" @click="back">Anterior</vs-button
      ><vs-button type="filled" @click="next">Siguiente</vs-button>
    </div>
  </div>
</template>
<script>
import StepProgress from "vue-step-progress";
import "vue-step-progress/dist/main.css";
import FormUserInfo from "./FormUserInfo.vue";
import ConsultReason from "./ConsultReason.vue";
export default {
  components: {
    "step-progress": StepProgress,
    FormUserInfo,
    ConsultReason,
  },
  data() {
    return {
      steps: ["Datos del paciente", "Datos de la consulta"],
      currentStep: 0,
    };
  },
  methods: {
    next() {
      this.currentStep++;
    },
    back() {
      this.currentStep--;
    },
  },
};
</script>
<style>
.step-progress__step-label {
  font-size: 10px;
}
.step-progress__step:after {
  width: 50px;
  height: 50px;
}
.step-progress__step span {
  font-size: 30px;
}
</style>
