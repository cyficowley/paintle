<template>
  <div class="relative bg-white">
    <div class="mx-auto px-4 sm:px-6">
      <div
        class="
          flex
          justify-between
          items-center
          border-b-2 border-gray-100
          py-6
          md:justify-start md:space-x-10
        "
      >
        <div class="flex justify-start lg:w-0 lg:flex-1">
          <img class="h-10 w-auto" src="/brush.svg" alt="" />
        </div>
        <div class="md:flex space-x-10">
          <h1 class="text-5xl text-gray-500">Paintle</h1>
        </div>
        <div class="md:flex items-center justify-end md:flex-1 lg:w-0">
          <button
            v-if="won"
            class="
              ml-8
              whitespace-nowrap
              inline-flex
              text-2xl
              items-center
              justify-center
              px-4
              py-2
              border border-transparent
              rounded-md
              shadow-sm
              font-medium
              text-white
              bg-limey-dark
              hover:bg-limey
            "
            @click="$emit('winner')"
          >
            Results
          </button>
          <button
            class="
              ml-8
              whitespace-nowrap
              inline-flex
              text-2xl
              items-center
              justify-center
              px-4
              py-2
              border border-transparent
              rounded-md
              shadow-sm
              font-medium
              text-white
              bg-limey-dark
              hover:bg-limey
            "
            @click="$emit('directions')"
          >
            Directions
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    won: {
      type: Boolean,
      required: true,
    },
  },
}
</script>