<template>
  <div class="mx-auto bg-white">
    <div class="text-2xl sm:text-5xl text-gray-500 mx-auto pb-4">
      <p>Quite the Aesthete!</p>
    </div>
    <div class="text-lg sm:text-2xl text-gray-400">
      <p>
        You successfully guessed today's Paintle with
        {{ guesses.length - 1 < 3 ? 'only' : '' }}
        <span class="font-bold">{{ guesses.length - 1 }} tile(s)</span>
        revealed!
      </p>
      <br />
      <p>Time until next Paintle: {{ secTillMidnightString }}</p>
    </div>
    <button
      class="
        mt-4
        px-4
        text-lg
        sm:text-2xl
        py-2
        border border-transparent
        rounded-md
        shadow-sm
        text-white
        bg-limey-dark
        hover:bg-limey
      "
      @click="copyResults"
    >
      Copy results
    </button>
  </div>
</template>

<script>
import copy from 'copy-to-clipboard'

export default {
  props: {
    guesses: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      secTillMidnight: 0,
    }
  },
  computed: {
    secTillMidnightString() {
      const hoursTillMidnight = Math.floor(this.secTillMidnight / 3600)
        .toString()
        .padStart(2, '0')
      const minsTillMidnight = (Math.floor(this.secTillMidnight / 60) % 60)
        .toString()
        .padStart(2, '0')
      const secsTillMidnight = (Math.floor(this.secTillMidnight) % 60)
        .toString()
        .padStart(2, '0')

      return `${hoursTillMidnight}:${minsTillMidnight}:${secsTillMidnight}`
    },
  },
  created() {
    const now = new Date()
    const midnight = new Date(
      now.getFullYear(),
      now.getMonth(),
      now.getDate(),
      23,
      59,
      59,
      999
    )

    this.secTillMidnight = Math.ceil(
      (midnight.getTime() - now.getTime()) / 1000
    )
    this.secTillMidnightTimer()
  },
  methods: {
    copyResults() {
      const options = {
        year: '2-digit',
        month: 'numeric',
        day: 'numeric',
      }
      const now = new Date()
      const dateString = now.toLocaleDateString('en-US', options)
      let text = `www.paintle.art ${dateString}\n`
      text += 'Revealed ' + (this.guesses.length - 1) + ' / 16 tiles\n\n'
      const unRevealedSquare = '⬜'
      const revealedSquare = '🟦'

      for (let x = 0; x < 16; x++) {
        if (this.guesses.includes(x)) {
          text += revealedSquare
        } else {
          text += unRevealedSquare
        }
        if (x % 4 === 3) {
          text += '\n'
        }
      }

      copy(text)
    },
    secTillMidnightTimer() {
      if (this.secTillMidnight > 0) {
        setTimeout(() => {
          this.secTillMidnight -= 1
          this.secTillMidnightTimer()
        }, 1000)
      }
    },
  },
}
</script>