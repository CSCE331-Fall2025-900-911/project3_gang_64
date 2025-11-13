import {
  mdiTimerSand,
  mdiWeatherCloudy,
  mdiWeatherFog,
  mdiWeatherLightning,
  mdiWeatherPartlyCloudy,
  mdiWeatherRainy,
  mdiWeatherSnowy,
  mdiWeatherSunny,
} from '@mdi/js';

export const WEATHER_LOCATION = {
  lat: 30.628,
  lon: -96.334,
  units: 'imperial',
};

const iconMap: Record<string, string> = {
  '01d': mdiWeatherSunny,
  '02d': mdiWeatherPartlyCloudy,
  '03d': mdiWeatherCloudy,
  '04d': mdiWeatherCloudy,
  '09d': mdiWeatherRainy,
  '10d': mdiWeatherRainy,
  '11d': mdiWeatherLightning,
  '13d': mdiWeatherSnowy,
  '50d': mdiWeatherFog,
  default: mdiTimerSand,
};

type WeatherData = {
  weather?: { icon: string }[];
};

export function getWeatherIcon(weatherData: WeatherData | undefined): string {
  if (!weatherData) {
    return iconMap.default;
  }

  const iconCode = weatherData?.weather?.[0]?.icon;

  if (iconCode && iconMap[iconCode]) {
    return iconMap[iconCode];
  }

  return iconMap.default;
}
