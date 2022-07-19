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
                "primary-200": "#90D4D1",
                "primary-300": "#23BDD2",
                primary: "#14A0C4",
                "primary-shade": "#a1d9e7",
            },
        },
    },
    plugins: [
        require("@tailwindcss/typography"),
        require("@tailwindcss/line-clamp"),
    ],
};
