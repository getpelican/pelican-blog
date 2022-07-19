/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./themes/**/*.html", "./themes/**/*.js"],
    theme: {
        extend: {
            fontFamily: {
                sans: ["Poppins", "sans-serif"],
            },
            colors: {
                "primary-100": "#F0F9F8",
                "primary-200": "#23BDD2",
                primary: "#14A0C4",
            },
        },
    },
    plugins: [
        require("@tailwindcss/typography"),
        require("@tailwindcss/line-clamp"),
    ],
};
