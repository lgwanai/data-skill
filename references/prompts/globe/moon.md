## 图表类型：月球 (Moon)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 图片资源提示
该图表需要加载以下类型的图片资源：
https://echarts.apache.org/examples/data-gl/asset/moon-base.jpg
https://echarts.apache.org/examples/data-gl/asset/moon-bump.jpg
https://echarts.apache.org/examples/data-gl/asset/starfield.jpg
https://echarts.apache.org/examples/data-gl/asset/pisa.hdr
请在生成代码时保留图片 URL 参数位置，并在最终输出时明确提示用户提供相应的图片资源 URL。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  globe: {
    baseTexture: ROOT_PATH + '/data-gl/asset/moon-base.jpg',
    heightTexture: ROOT_PATH + '/data-gl/asset/moon-bump.jpg',
    displacementScale: 0.05,
    displacementQuality: 'medium',
    environment: ROOT_PATH + '/data-gl/asset/starfield.jpg',
    shading: 'realistic',
    realisticMaterial: {
      roughness: 0.8,
      metalness: 0
    },
    postEffect: {
      enable: true,
      SSAO: {
        enable: true,
        radius: 2,
        intensity: 1,
        quality: 'high'
      }
    },
    temporalSuperSampling: {
      enable: true
    },
    light: {
      ambient: {
        intensity: 0
      },
      main: {
        intensity: 2,
        shadow: true
      },
      ambientCubemap: {
        texture: ROOT_PATH + '/data-gl/asset/pisa.hdr',
        exposure: 0,
        diffuseIntensity: 0.02
      }
    },
    viewControl: {
      autoRotate: false
    }
  },
  series: []
};
```

