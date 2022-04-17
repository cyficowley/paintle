<template>
  <div class="relative bg-white flex">
    <!-- <p>guess is: {{ guess }}</p> -->
    <div class="absolute w-full top-0">
      <Results
        v-if="guess.length !== 0 && !canSubmit"
        :results="filteredPaintings"
        class="absolute w-full bottom-0 mb-2"
        @selected="setGuess"
      />
    </div>
    <input
      v-model="guess"
      type="text"
      :placeholder="
        canGuess
          ? 'Search for artist / painting'
          : 'Please select a tile to reveal'
      "
      :disabled="!canGuess"
      class="
        border-4 border-bluey
        rounded-2xl
        text-2xl
        outline-none
        w-full
        px-4
        py-3
        text-gray-500
      "
      @keyup.enter="checkEnter"
    />
    <button
      class="rounded-2xl text-2xl outline-none ml-4 px-4 py-4 text-white"
      :class="canSubmit ? 'hover:bg-bluey-dark bg-bluey' : 'bg-bluey-light'"
      @click="guessed"
    >
      Submit
    </button>
  </div>
</template>


<script>
export default {
  name: 'GuesserItem',
  props: {
    allAnswers: {
      type: Array,
      required: true,
    },
    canGuess: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      guess: '',
      results: [],
    }
  },
  computed: {
    filteredPaintings() {
      const filteredPaintings = this.allAnswers.filter((painting) => {
        return (
          painting.artist.toLowerCase().includes(this.guess.toLowerCase()) ||
          painting.name.toLowerCase().includes(this.guess.toLowerCase())
        )
      })
      return filteredPaintings
    },
    canSubmit() {
      return (
        this.canGuess &&
        this.allAnswers.some((painting) => {
          return painting.name.toLowerCase() === this.guess.toLowerCase()
        })
      )
    },
  },
  methods: {
    setGuess(guess) {
      this.guess = guess.name
    },
    guessed() {
      this.$emit('guessed', this.guess)
      this.guess = ''
    },
    checkEnter() {
      if (this.filteredPaintings.length === 1) {
        this.guess = this.filteredPaintings[0].name
      }
      if (this.canSubmit) {
        this.guessed()
      }
    },
  },
}
</script>