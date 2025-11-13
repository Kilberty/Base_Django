import {defineConfig} from "vite"
import vue from "@vitejs/plugin-vue"
import path from "path"

export default defineConfig({
    plugins :[
        vue()
    ],
    resolve:{
        alias:{
            '@':path.resolve('resources/js')
        }
    },
    base:'/static/',
    build:{
        outDir:'static/build',
        rollupOptions:{
            input:[
                'resources/js/app.js',
            ]
        }
    }
})