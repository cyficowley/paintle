<template>
  <div class="border-4 border-bluey-dark rounded-2xl bg-white px-4 py-3">
    <div v-if="results.length !== 0">
      <p
        v-for="result in results.slice(0, 6)"
        :key="result.name"
        class="text-lg sm:text-xl text-gray-500 hover:bg-limey"
        @click="emitValue(result)"
      >
        <span class="font-bold">{{ result.name }}</span> - {{ result.artist }}
      </p>
    </div>
    <div v-else>
      <p class="text-lg sm:text-xl text-gray-500">No results found</p>
    </div>
  </div>
</template>


<script>
export default {
  name: 'GuesserItem',
  props: {
    results: {
      type: Array,
      required: true,
    },
  },
  methods: {
    emitValue(result) {
      this.$emit('selected', result)
    },
  },
}
</script>