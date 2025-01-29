<script setup lang="ts">
import { ref, watch, computed } from 'vue'

const code = ref('')
const isValid = ref(false)
const error = ref('')
const loading = ref(false)
const showResults = ref(false)
const lookupData = ref({})
const showHelp = ref(false)
const resultsRef = ref(null)

// Simplified validation logic
const isValidCode = computed(() => {
  const cleaned = code.value.replace(/\s/g, '')
  return cleaned.length === 19 && /^\d{19}$/.test(cleaned)
})

// Remove individual validation functions and use computed property
const validateCode = () => {
  const cleaned = code.value.replace(/\s/g, '')
  if (cleaned.length !== 19) return 'Please enter all 19 digits'
  if (!/^\d+$/.test(cleaned)) return 'Numbers only please'
  return true
}

// Updated submit handler
const submitCode = async () => {
  if (!isValidCode.value) return
  loading.value = true
  error.value = ''
  try {
    // Simulating lookup with more realistic data
    setTimeout(() => {
      lookupData.value = {
        clinicName: 'Example Veterinary',
        address: '100 Street Name, Town, County, Post Code',
        phone: '0118-999-881-999-119-725-3',
        email: 'contact@examplevets.com',
        hours: 'Open 24/7 for Emergencies',
        lastScan: '2024-01-15 14:30 PST',
        location: {
          lat: 38.5816,
          lng: -121.4944
        }
      }
      showResults.value = true
      loading.value = false
      
      // Smooth scroll after results are shown
      setTimeout(() => {
        resultsRef.value?.$el.scrollIntoView({
          behavior: 'smooth',
          block: 'center'
        })
      }, 100)
    }, 1500)
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
    <v-main class="bg-grey-lighten-4">
      <v-container fluid>
        <div class="d-flex flex-column align-center py-8 gap-6">
          <!-- Main Search Card -->
          <v-card
            max-width="700"
            min-width="600"
            class="mx-auto elevation-3 rounded-lg position-relative overflow-hidden"
          >
            <!-- Decorative top border -->
            <div class="gradient-border"></div>

            <!-- Help Dialog -->
            <v-dialog v-model="showHelp" max-width="400">
              <template v-slot:activator="{ props }">
                <v-btn
                  icon
                  variant="text"
                  v-bind="props"
                  class="position-absolute right-2 top-2 help-button"
                  size="small"
                >
                  <v-icon>mdi-help-circle-outline</v-icon>
                </v-btn>
              </template>
              <v-card>
                <v-card-title class="text-h6"> Need help finding the RFID code? </v-card-title>
                <v-card-text>
                  The RFID code can be scanned using a microchip reader at any veterinary clinic or
                  animal shelter. If you've found a lost pet, you can take them to the nearest vet or
                  shelter to have their chip scanned.
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="primary" variant="text" @click="showHelp = false">Got it</v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>

            <v-card-text class="pa-8">
              <h2 class="text-h4 mb-2 text-center font-weight-bold">🐾 Microchip Lookup</h2>
              <p class="text-subtitle-1 text-center text-grey-darken-1 mb-6">
                Find a pet's veterinary clinic using their microchip number
              </p>

              <v-form @submit.prevent="submitCode">
                <v-text-field
                  v-model="code"
                  :rules="[validateCode]"
                  placeholder="Enter 19-digit microchip number"
                  variant="outlined"
                  :error-messages="error"
                  class="mb-6 search-input"
                  maxlength="23"
                  density="comfortable"
                  bg-color="white"
                  height="64"
                  :style="{ fontSize: '1.25rem' }"
                ></v-text-field>

                <v-btn
                  block
                  color="primary"
                  size="x-large"
                  type="submit"
                  :loading="loading"
                  :disabled="!isValidCode"
                  class="search-button"
                  height="56"
                  elevation="2"
                >
                  <template v-slot:loader>
                    <v-progress-circular indeterminate color="white"></v-progress-circular>
                  </template>
                  <div class="d-flex align-center justify-center w-100">
                    <span class="search-text">Find Veterinary Clinic</span>
                    <v-icon class="search-icon ms-3" size="large">mdi-magnify</v-icon>
                  </div>
                </v-btn>
              </v-form>
            </v-card-text>
          </v-card>

          <!-- Results Card -->
          <v-expand-transition>
            <v-card
              v-if="showResults"
              ref="resultsRef"
              max-width="700"
              min-width="600"
              class="mx-auto elevation-3 rounded-lg results-card"
            >
              <div class="gradient-border"></div>
              <v-card-title class="d-flex align-center pa-4">
                <v-icon color="success" class="me-2">mdi-check-circle</v-icon>
                <span class="text-h5">Veterinary Clinic Found</span>
                <v-spacer></v-spacer>
                <v-btn icon variant="text" @click="showResults = false">
                  <v-icon>mdi-close</v-icon>
                </v-btn>
              </v-card-title>

              <v-card-text class="pa-6">
                <div class="clinic-details mb-6">
                  <h3 class="text-h5 mb-4">{{ lookupData.clinicName }}</h3>
                  <div class="detail-item">
                    <v-icon class="me-2">mdi-map-marker</v-icon>
                    {{ lookupData.address }}
                  </div>
                  <div class="detail-item">
                    <v-icon class="me-2">mdi-phone</v-icon>
                    {{ lookupData.phone }}
                  </div>
                  <div class="detail-item">
                    <v-icon class="me-2">mdi-email</v-icon>
                    {{ lookupData.email }}
                  </div>
                  <div class="detail-item">
                    <v-icon class="me-2">mdi-clock</v-icon>
                    {{ lookupData.hours }}
                  </div>
                  <div class="mt-4 pt-4 border-t">
                    <small class="text-grey">Last scanned: {{ lookupData.lastScan }}</small>
                  </div>
                </div>

                <!-- Google Maps Integration -->
                <v-card class="map-container mb-4" elevation="1">
                  <iframe
                    width="100%"
                    height="300"
                    style="border:0"
                    loading="lazy"
                    allowfullscreen
                    :src="`https://www.google.com/maps/embed/v1/place?key=YOUR_API_KEY&q=${encodeURIComponent(lookupData.address)}`"
                  ></iframe>
                </v-card>
              </v-card-text>
            </v-card>
          </v-expand-transition>
        </div>
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped>
.min-height-screen {
  min-height: 100vh;
}

.position-absolute {
  position: absolute;
}

.search-button {
  transition: all 0.3s ease;
  font-size: 1.25rem;
}

.search-text {
  transition: transform 0.3s ease;
  letter-spacing: 0.5px;
}

.search-icon {
  transition: transform 0.3s ease;
}

.search-button:hover:not(:disabled) .search-icon {
  transform: translateX(4px) scale(1.1);
}

.search-button:hover:not(:disabled) .search-text {
  transform: translateX(-2px);
}

.help-button {
  opacity: 0.6;
  transition: opacity 0.3s ease;
}

.help-button:hover {
  opacity: 1;
}

.gradient-border {
  height: 4px;
  background: linear-gradient(to right, #1867c0, #5cbbf6);
}

.search-input {
  border-radius: 12px;
}

.detail-item {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
  color: #424242;
}

.border-t {
  border-top: 1px solid #e0e0e0;
}

/* Optional: Add a subtle hover effect to the main card */
.v-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.v-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1) !important;
}

.results-card {
  animation: slideIn 0.5s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.gap-6 {
  gap: 1.5rem;
}

.map-container {
  border-radius: 12px;
  overflow: hidden;
}
</style>
