// Centralized HTTP communication with the FastAPI backend.
// Components should never call fetch() directly - they go through these functions.

const API_BASE_URL = 'http://localhost:8000'

/**
 * Checks whether the backend API is reachable and healthy.
 * Returns true/false instead of throwing, since this is only used
 * for displaying a status indicator, not for error handling flows.
 */
export async function checkHealth() {
  try {
    const response = await fetch(`${API_BASE_URL}/health`)
    if (!response.ok) return false

    const data = await response.json()
    return data.status === 'ok'
  } catch {
    return false
  }
}

/**
 * Runs the full analyze -> refactor -> review workflow on the backend.
 * Throws an Error with a user-facing message on failure.
 */
export async function analyzeCode(language, code) {
  let response
  try {
    response = await fetch(`${API_BASE_URL}/analyze`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ language, code }),
    })
  } catch {
    throw new Error('Could not reach the backend. Make sure the API server is running.')
  }

  if (!response.ok) {
    let message = `Request failed with status ${response.status}.`
    try {
      const errorBody = await response.json()
      if (errorBody?.detail) {
        message = errorBody.detail
      }
    } catch {
      // response had no JSON body, keep the generic message
    }
    throw new Error(message)
  }

  return response.json()
}
