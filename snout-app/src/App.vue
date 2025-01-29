<script setup lang="ts">
import { ref, watch, computed } from 'vue'

const code = ref('')
const isValid = ref(false)
const error = ref('')
const loading = ref(false)
const showResults = ref(false)
const lookupData = ref({})
const showHelp = ref(false) // New reactive property for toggling help section

// Add computed property for cleaned code
const cleanedCode = computed(() => code.value.replace(/\s/g, ''))

// Update validation functions
const validateLength = (value: string) => {
  const cleaned = value.replace(/\s/g, '')
  return cleaned.length === 19 || 'Code must be exactly 19 digits'
}

const validateDigits = (value: string) => {
  const cleaned = value.replace(/\s/g, '')
  return /^\d{19}$/.test(cleaned) || 'Code must contain only digits'
}

// Updated submitCode function to handle spaces in validation
const submitCode = async () => {
  const cleanCode = code.value.replace(/\s/g, '') // Remove spaces before validation
  if (!isValid.value || !/^\d{19}$/.test(cleanCode)) {
    error.value = 'Please enter a valid 19-digit numerical code.'
    return
  }
  loading.value = true
  error.value = ''
  try {
    // Perform lookup (replace with actual lookup logic)
    // Example:
    // const response = await fetch(`/api/lookup?code=${code.value}`)
    // lookupData.value = await response.json()
    // Simulating lookup
    setTimeout(() => {
      lookupData.value = { code: code.value, detail: 'Sample Detail Information' }
      showResults.value = true
      loading.value = false
    }, 2000)
  } catch (err) {
    error.value = 'Lookup failed. Please try again.'
    loading.value = false
  }
}

// Watcher to format input and restrict to 19 digits
watch(code, (newValue) => {
  const digits = newValue.replace(/\D/g, '').slice(0, 19) // Allow only digits and limit to 19
  const spaced = digits.replace(/(\d{4})(?=\d)/g, '$1 ').trim()
  if (spaced !== newValue) {
    code.value = spaced
  }
})
</script>

<template>
  <v-app>
    <v-main>
      <v-container class="d-flex flex-column align-center py-8" fluid>
        <!-- Page Title -->
        <h1 class="text-h3 mb-2">Lost Pet Finder</h1>
        <p class="text-subtitle-1 text-center mx-auto mb-4">
          Enter the 19-digit RFID code to find your pet’s veterinary practice
        </p>

        <!-- Main Card -->
        <v-card max-width="600" class="w-100 pa-4">
          <v-card-title class="pb-0">RFID Scanner</v-card-title>
          <v-card-subtitle>Enter the 19-digit microchip code below</v-card-subtitle>
          <v-card-text>
            <v-form ref="form" v-model="isValid" @submit.prevent="submitCode" class="mb-4">
              <v-text-field
                v-model="code"
                label="RFID Code"
                :rules="[validateLength, validateDigits]"
                placeholder="0000 0000 0000 0000 000"
                required
                maxlength="23"
                class="mb-3"
              >
              </v-text-field>

              <!-- Error Alert -->
              <v-alert
                v-if="error"
                type="error"
                dismissible
                class="mb-4"
                @dismissed="error = ''"
              >
                {{ error }}
              </v-alert>

              <v-btn
                :disabled="!isValid || loading"
                color="primary"
                type="submit"
                class="submit-button"
              >
                <div class="d-flex align-center">
                  <span class="button-text" v-if="!loading">Find Veterinary Practice</span>
                  <v-progress-circular
                    v-else
                    indeterminate
                    size="20"
                    color="white"
                  ></v-progress-circular>
                  <!-- Arrow Icon for Hover -->
                  <v-icon class="arrow-icon ms-2">mdi-arrow-right</v-icon>
                </div>
              </v-btn>
            </v-form>

            <!-- Results Dialog Triggered on showResults -->
            <v-dialog v-model="showResults" transition="fade-transition" max-width="600px">
              <v-card>
                <v-card-title>
                  <v-icon left color="green">mdi-check</v-icon>
                  Veterinary Practice Found
                </v-card-title>
                <v-card-text>
                  {{ lookupData }}
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="showResults = false">Close</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-card-text>
        </v-card>

        <!-- Toggleable Help Section -->
        <v-btn text color="blue" class="mt-4" @click="showHelp = !showHelp">
          Need help?
        <v-icon right>mdi-chevron-down</v-icon>
        </v-btn>

        <v-collapse v-if="showHelp" class="help-section">
          <v-card color="blue-lighten-4" class="pa-4" max-width="600">
            <v-card-title class="text-h6">Need help finding the RFID code?</v-card-title>
            <v-card-text class="text-body-1">
              The RFID code can be scanned using a microchip reader at any veterinary clinic or animal shelter.
              If you’ve found a lost pet, you can take them to the nearest vet or shelter to have their chip scanned.
            </v-card-text>
          </v-card>
        </v-collapse>
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}

/* Submit Button Visual Cue */
.submit-button {
  position: relative;
  transition: background-color 0.3s ease;
  min-width: 250px; /* Ensure minimum width */
}

.button-text {
  transition: opacity 0.3s ease;
  margin-right: 24px; /* Add space for the arrow */
}

.submit-button:hover .button-text {
  opacity: 0.8;
}

.submit-button:hover .arrow-icon {
  transform: translateX(5px);
}

.arrow-icon {
  transition: transform 0.3s ease;
}

/* Help Section Animation */
.help-section {
  transition: max-height 0.5s ease, opacity 0.5s ease;
  overflow: hidden;
}
</style>
