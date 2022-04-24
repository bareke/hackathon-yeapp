<template>
  <div class="rounded shadow-xl bg-blue-100 p-8 w-1/2">
    <h1 class="text-sm sm:text-xl font-bold mb-5">Adjuntar anexos</h1>

    <label for="annexes">
      Agregar examenes o anexos similares<input
        class="border-dotted border-2 border-black p-3"
        id="annexes"
        type="file"
        multiple
      />
    </label>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
  methods: {
    myListener(myArg, transferData, nativeEvent) {
      console.log(myArg);
      console.log(transferData);
      console.log(nativeEvent);
      // myArg === 'foo'
    },
  },
};
</script>
<style scoped>
input[type="file"] + button {
  display: hidden;
}
</style>
