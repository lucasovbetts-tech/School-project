document.addEventListener('DOMContentLoaded', () => {
    const mainHeader = document.querySelector('.main-header');

    if (!mainHeader) {
        console.error('Main Header was not found.');
        return;
    }

    mainHeader.innerHTML = `
        <header class="site-header">
            <nav class="site-nav" aria-label="Main navigation">
                <img id="CostaLogoImg" src="/static/CostaCoffeeLogo.png" alt="Costa Coffee">
                <a class="nav-button" href="/Home">Home</a>
                <a class="nav-button" href="/About">About</a>
                <a class="nav-button" href="/Contact">Contact</a>
            </nav>
        </header>
    `;
});
