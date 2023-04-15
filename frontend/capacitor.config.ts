import {CapacitorConfig} from '@capacitor/cli';

const config: CapacitorConfig = {
    appId: 'yarvod.finaflow',
    appName: 'frontend',
    webDir: 'dist',
    bundledWebRuntime: false,
    server: {
        hostname: "finaflow.ru",
        iosScheme: "https",
        androidScheme: "https",
        url: "https://finaflow.ru"
    }
};

export default config;
