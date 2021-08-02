// vue.config.js
module.exports = {
    lintOnSave: process.env.NODE_ENV !== 'production',
    runtimeCompiler: true,

    pluginOptions: {
        i18n: {
            locale: 'fr',
            fallbackLocale: 'en',
            localeDir: 'locales',
            enableInSFC: true,
        },
    },
    devServer: {
        disableHostCheck: true,
    },
}
