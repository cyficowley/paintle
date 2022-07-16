<template>
    <div class="relative bg-white">
        <div class="mx-auto px-4 sm:px-6">
            <div class="
          flex
          justify-between
          items-center
          border-b-2 border-gray-100
          sm:py-6
          py-3
          md:justify-start md:space-x-10
        ">
                <div class="flex justify-start lg:w-0 lg:flex-1">
                    <img class="h-8 sm:h-10 w-auto" src="/brush.svg" alt="" />
                </div>
                <div class="md:flex space-x-10 px-2 sm:px-0">
                    <h1 class="text-2xl sm:text-5xl text-gray-500">Cycle</h1>
                </div>
                <div class="sm:flex-grow-0 flex-grow"></div>
                <div class="md:flex items-center justify-end md:flex-1 lg:w-0">
                    <button v-if="won || lost" class="
              sm:ml-8
              whitespace-nowrap
              inline-flex
              sm:text-2xl
              text-md
              items-center
              justify-center
              sm:px-4 sm:py-2
              py-1
              px-2
              border border-transparent
              rounded-md
              shadow-sm
              font-medium
              text-white
              bg-limey-dark
              hover:bg-limey
            " @click="$emit(won ? 'winner' : 'loser')">
                        Results
                    </button>

                    <button class="
              sm:ml-8
              whitespace-nowrap
              inline-flex
              sm:text-2xl
              text-md
              items-center
              justify-center
              sm:px-4 sm:py-2
              py-1
              px-2
              border border-transparent
              rounded-md
              shadow-sm
              font-medium
              text-white
              bg-limey-dark
              hover:bg-limey
            " @click="$emit('directions')">
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
        lost: {
            type: Boolean,
            required: true,
        },
    },
}
</script>
