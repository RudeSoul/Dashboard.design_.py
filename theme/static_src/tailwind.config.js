/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
  /**
   * Stylesheet generation mode.
   *
   * Set mode to "jit" if you want to generate your styles on-demand as you author your templates;
   * Set mode to "aot" if you want to generate the stylesheet in advance and purge later (aka legacy mode).
   */
  mode: "jit",

  purge: [
    /**
     * HTML. Paths to Django template files that will contain Tailwind CSS classes.
     */

    /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
    "../templates/**/*.html",

    /*
     * Main templates directory of the project (BASE_DIR/templates).
     * Adjust the following line to match your project structure.
     */
    "../../templates/**/*.html",

    /*
     * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
     * Adjust the following line to match your project structure.
     */
    "../../**/templates/**/*.html",

    /**
     * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
     * patterns match your project structure.
     */
    /* JS 1: Ignore any JavaScript in node_modules folder. */
    // '!../../**/node_modules',
    /* JS 2: Process all JavaScript files in the project. */
    // '../../**/*.js',

    /**
     * Python: If you use Tailwind CSS classes in Python, uncomment the following line
     * and make sure the pattern below matches your project structure.
     */
    // '../../**/*.py'
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      padding: {
        13: "3.125rem", // 50px
        paddingOne: "1px",
      },
      spacing: {
        15: "3.75rem", //60px;
      },
      width: {
        49: "12.5rem", // 200px
        sidebarWidth: "16.8125rem",
      },
      maxWidth: {
        column: "17rem", // 272px
      },
      minWidth: {
        column: "15rem", // 240px
      },
      outline: {
        grey: "1px solid #DDDDDD",
      },
      placeholderColor: {
        primary: "#BBBBBB",
      },
      textColor: {
        field: "#828282",
        label: "#5A5A5A",
        "table-head": "#9E9E9E",
        "table-detail": "#5A5A5A",
        "badge-draft": "#4D3B0E",
        "badge-staged": "#1F504D",
        "badge-active": "#385030",
        "badge-inactive": "#3E3E3E",
        primary: "#5A5A5A",
        dark: "#323232",
        white: "#ffffff",
        light: "#8E8E8E",
        gray70: "#5F5F5F",
        iconColor: "#8B8B8B",
        iconLight: "#BBBBBB",
        lightBlack: "#9E9E9E",
      },
      lineHeight: {
        "extra-loose": "3.5rem",
      },
      fontSize: {
        profileName: ["16px", "12px"],
        "14px": "0.875rem", //14px
        "20px": "1.25rem", //20px
        "2xl": "1.75rem", //28px
      },
      margin: {
        minus2: "-0.125rem", //-2px
        margin20: "1.25rem", //20px
        margin22: "1.375rem", //22 px
        margin42: "2.625rem", // 42px
        margin50: "3.125rem", //50px
      },
      zIndex: {
        m1: -1,
      },
      boxShadow: {
        navShadow: "0 4px 10px 0 rgba(0, 0, 0, 0.05)",
      },
      height: {
        emptyDiv: "1px",
      },
      borderColor: (theme) => ({
        ...theme("colors"),
        "green-heading": "#1AA861",
      }),
    },
    fontFamily: {
      inter: ["Inter", "ui-sans-serif", "system-ui"],
    },
    backgroundColor: (theme) => ({
      ...theme("colors"),
      primary: "#1AA861",
      gray: "#E5E5E5",
      checkbox: "#8AD1AD",
      "table-head": "#FAFAFA",
      "table-hover": "rgba(236,249,242,0.5)",
      "badge-draft": "#EBC35E",
      "badge-staged": "#5EEBE2",
      "badge-active": "#A9F38F",
      "badge-inactive": "#C0C0C0",
      bodyBackground: "#F6F5F6",
    }),
  },
  variants: {
    extend: {
      cursor: ["hover", "focus"],
      pointerEvents: ["hover", "focus"],
    },
  },
  plugins: [
    /**
     * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
     * for forms. If you don't like it or have own styling for forms,
     * comment the line below to disable '@tailwindcss/forms'.
     */
    require("@tailwindcss/forms"),
    require("@tailwindcss/typography"),
    require("@tailwindcss/line-clamp"),
    require("@tailwindcss/aspect-ratio"),
  ],
};
