<template>
  <div class="mx-auto bg-white">
    <div class="pb-4 mx-auto text-2xl text-gray-500 sm:text-5xl">
      <p>Aw Shucks. Better Luck Next Time?</p>
    </div>
    <div class="text-lg text-gray-400 sm:text-2xl">
      <p>You unfortunately were unable to guess the correct answer :(</p>
      <br />
      <p>The correct answer was:</p>
      <p>
        <span class="font-bold">{{ answer.name }}</span
        >.
      </p>
      <br />
      <p>Reload for the next cycle</p>
    </div>
    <button
      class="px-4 py-2 mt-4 text-lg text-white border border-transparent rounded-md shadow-sm  sm:text-2xl bg-limey-dark hover:bg-limey"
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
    answer: {
      type: Object,
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
      let text = `www.paintle.art/cycle ${dateString}\n`
      text += 'Revealed X / 16 tiles\n\n'
      const revealedSquare = '🟦'

      for (let x = 0; x < 16; x++) {
        text += revealedSquare
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
