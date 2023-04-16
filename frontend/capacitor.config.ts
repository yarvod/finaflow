import {CapacitorConfig} from '@capacitor/cli';

const config: CapacitorConfig = {
    appId: 'A1B2C3D4E5.com.yarvod.finaflow',
    appName: 'FinaFlow',
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
