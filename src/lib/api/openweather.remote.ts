import { query } from '$app/server';
import { env } from '$env/dynamic/private';

const OPENWEATHER_API_KEY = env.OPENWEATHER_API_KEY;
const BASE_URL = 'https://api.openweathermap.org/data/2.5/weather';

export interface CurrentWeatherParams {
  lat: number;
  lon: number;
  units?: 'metric' | 'imperial' | 'standard';
}

/**
 * Fetches current weather data using the OpenWeather API.
 * @param params - Latitude, Longitude, and optional units.
 * @returns The raw weather data response as a JSON object (or throws an error).
 */
async function fetchCurrentWeatherImpl({ lat, lon, units = 'metric' }: CurrentWeatherParams): Promise<any> {
  if (!OPENWEATHER_API_KEY) {
    throw new Error('Server Error: OPENWEATHER_API_KEY is not configured on the server.');
  }

  const url = `${BASE_URL}?lat=${lat}&lon=${lon}&units=${units}&appid=${OPENWEATHER_API_KEY}`;

  console.log(`Fetching current weather data from OpenWeather API for url: ${url}`);

  const response = await fetch(url);

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`OpenWeather API failed: ${response.status} - ${response.statusText}. Response: ${errorText}`);
  }

  return await response.json();
}

/**
 * @param fn - The actual server-side implementation function.
 * @param validate - Optionally, you can pass a Zod/Valibot schema here for input validation.
 */
export const fetchCurrentWeather = query('unchecked', fetchCurrentWeatherImpl);
