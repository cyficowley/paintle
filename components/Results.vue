<template>
  <div class="px-4 py-3 bg-white border-4 border-bluey-dark rounded-2xl">
    <div v-if="results.length !== 0">
      <p
        v-for="result in results.slice(0, 5)"
        :key="result.name"
        class="text-lg text-gray-500 sm:text-xl hover:bg-limey"
        @click="emitValue(result)"
      >
        <span class="font-bold">{{ result.name }}</span
        ><span v-if="hasArtist"> - {{ result.artist }}</span>
      </p>
    </div>
    <div v-else>
      <p class="text-lg text-gray-500 sm:text-xl">No results found</p>
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
    hasArtist: {
      type: Boolean,
      default: true,
    },
  },
  methods: {
    emitValue(result) {
      this.$emit('selected', result)
    },
  },
}
</script>