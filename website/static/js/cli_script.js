document.addEventListener('DOMContentLoaded', function() {
    const linuxShells = ['bash', 'shell', 'PowerShell'];
    const windowsShells = ['CMD', 'PowerShell'];

    document.getElementById('linux').onclick = () => updateShellOptions(linuxShells);
    document.getElementById('windows').onclick = () => updateShellOptions(windowsShells);

    function updateShellOptions(options) {
        const shellOptionsDiv = document.getElementById('shell-options');
        shellOptionsDiv.innerHTML = '';
        options.forEach(shell => {
            const label = document.createElement('label');
            label.htmlFor = shell;
            label.textContent = shell;
            const input = document.createElement('input');
            input.type = 'radio';
            input.id = shell;
            input.name = 'shell_env';
            input.value = shell;
            if (options.indexOf(shell) === 0) {
                input.checked = true;
            }
            shellOptionsDiv.appendChild(input);
            shellOptionsDiv.appendChild(label);
        });
    }

    // Initialize shell options based on the default OS selection
    updateShellOptions(linuxShells);
});
