import { query } from '$app/server';
import { env } from '$env/dynamic/private';
import * as v from 'valibot';

const BASE_URL = 'https://api.openweathermap.org/data/2.5/weather';

export interface CurrentWeatherParams {
  lat: number;
  lon: number;
  units?: 'metric' | 'imperial' | 'standard';
}

const currentWeatherParams = v.object({
  lat: v.number(),
  lon: v.number(),
  units: v.optional(v.union([v.literal('metric'), v.literal('imperial'), v.literal('standard')]), 'metric'),
});

export const fetchCurrentWeather = query(currentWeatherParams, async ({ lat, lon, units = 'metric' }) => {
  const url = `${BASE_URL}?lat=${lat}&lon=${lon}&units=${units}&appid=${env.OPENWEATHER_API_KEY}`;

  const response = await fetch(url);

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`OpenWeather API failed: ${response.status} - ${response.statusText}. Response: ${errorText}`);
  }

  return await response.json();
});
