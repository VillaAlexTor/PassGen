const passwordDisplay = document.getElementById('password-display');
const lengthSlider = document.getElementById('length');
const lengthVal = document.getElementById('length-val');
const uppercaseEl = document.getElementById('uppercase');
const lowercaseEl = document.getElementById('lowercase');
const numbersEl = document.getElementById('numbers');
const symbolsEl = document.getElementById('symbols');
const generateBtn = document.getElementById('generate-btn');
const copyBtn = document.getElementById('copy-btn');

const CHAR_SETS = {
    uppercase: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    lowercase: 'abcdefghijklmnopqrstuvwxyz',
    numbers: '0123456789',
    symbols: '!@#$%^&*()_+~`|}{[]:;?><,./-='
};

// Actualizar valor de longitud en el UI
lengthSlider.addEventListener('input', () => {
    lengthVal.textContent = lengthSlider.value;
});

// Función de generación segura
function generatePassword() {
    let charset = '';
    if (uppercaseEl.checked) charset += CHAR_SETS.uppercase;
    if (lowercaseEl.checked) charset += CHAR_SETS.lowercase;
    if (numbersEl.checked) charset += CHAR_SETS.numbers;
    if (symbolsEl.checked) charset += CHAR_SETS.symbols;

    if (charset === '') {
        alert('Por favor selecciona al menos un tipo de caracteres.');
        uppercaseEl.checked = true;
        return generatePassword();
    }

    let password = '';
    const array = new Uint32Array(parseInt(lengthSlider.value));
    
    // Usar window.crypto para aleatoriedad criptográficamente segura
    window.crypto.getRandomValues(array);

    for (let i = 0; i < array.length; i++) {
        password += charset.charAt(array[i] % charset.length);
    }

    passwordDisplay.textContent = password;
}

// Copiar al portapapeles
copyBtn.addEventListener('click', () => {
    const password = passwordDisplay.textContent;
    if (!password) return;

    navigator.clipboard.writeText(password).then(() => {
        // Feedback visual simple
        const originalIcon = copyBtn.innerHTML;
        copyBtn.innerHTML = '<i data-lucide="check" style="color: #4ade80"></i>';
        lucide.createIcons();
        
        setTimeout(() => {
            copyBtn.innerHTML = originalIcon;
            lucide.createIcons();
        }, 2000);
    });
});

// Event Listeners
generateBtn.addEventListener('click', generatePassword);

// Generar una contraseña inicial
window.addEventListener('DOMContentLoaded', generatePassword);
