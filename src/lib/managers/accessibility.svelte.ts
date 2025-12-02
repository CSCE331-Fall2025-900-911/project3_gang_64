export type ColorblindMode = 'normal' | 'protanopia' | 'deuteranopia' | 'tritanopia' | 'grayscale';

const colorblindModes: ColorblindMode[] = ['normal', 'protanopia', 'deuteranopia', 'tritanopia', 'grayscale'];

function applyColorblindClass(mode: ColorblindMode) {
  if (typeof document === 'undefined') return;

  // Remove all colorblind classes
  for (const m of colorblindModes) {
    document.documentElement.classList.remove(`colorblind-${m}`);
  }

  // Add the new class (except for normal which needs no filter)
  if (mode !== 'normal') {
    document.documentElement.classList.add(`colorblind-${mode}`);
  }
}

export function initializeColorblindMode() {
  const saved = localStorage.getItem('colorblindMode');
  if (saved) {
    accessibilityManager.colorblindMode = saved as ColorblindMode;
    applyColorblindClass(saved as ColorblindMode);
  }
}

class AccessibilityManager {
  colorblindMode = $state<ColorblindMode>('normal');

  setColorblindMode(mode: ColorblindMode) {
    this.colorblindMode = mode;
    localStorage.setItem('colorblindMode', mode);
    applyColorblindClass(mode);
  }
}

export const accessibilityManager = new AccessibilityManager();
