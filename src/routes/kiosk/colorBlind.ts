import { writable } from 'svelte/store';

export type ColorblindMode = 'normal' | 'protanopia' | 'deuteranopia' | 'tritanopia' | 'grayscale';
export const colorblindMode = writable<ColorblindMode>('normal');
