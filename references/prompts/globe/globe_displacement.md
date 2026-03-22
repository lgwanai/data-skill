## 图表类型：地形位移 (Globe Displacement)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 图片资源提示
该图表需要加载以下类型的图片资源：
https://echarts.apache.org/examples/data-gl/asset/bathymetry_bw_composite_4k.jpg
https://echarts.apache.org/examples/data-gl/asset/pisa.hdr
请在生成代码时保留图片 URL 参数位置，并在最终输出时明确提示用户提供相应的图片资源 URL。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  globe: {
    displacementTexture:
      ROOT_PATH + '/data-gl/asset/bathymetry_bw_composite_4k.jpg',
    displacementScale: 0.1,
    displacementQuality: 'ultra',
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
        intensity: 1.5,
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
        intensity: 1,
        shadow: true
      },
      ambientCubemap: {
        texture: ROOT_PATH + '/data-gl/asset/pisa.hdr',
        exposure: 1,
        diffuseIntensity: 0.2
      }
    },
    viewControl: {
      autoRotate: false
    },
    debug: {
      wireframe: {
        show: true
      }
    }
  },
  series: []
};
```

