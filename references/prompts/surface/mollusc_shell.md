## 图表类型： (Mollusc Shell)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 图片资源提示
该图表需要加载以下类型的图片资源：
https://echarts.apache.org/examples/data-gl/asset/canyon.hdr
请在生成代码时保留图片 URL 参数位置，并在最终输出时明确提示用户提供相应的图片资源 URL。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
option = {
  tooltip: {},
  visualMap: {
    show: false,
    dimension: 2,
    min: -5,
    max: 0,
    inRange: {
      color: [ /* 请使用用户的真实数据数组替换此处 */ ]
    }
  },
  xAxis3D: {},
  yAxis3D: {},
  zAxis3D: {},
  grid3D: {
    show: true,
    postEffect: {
      enable: true
    },
    temporalSuperSampling: {
      enable: true
    },
    light: {
      main: {
        intensity: 3,
        shadow: true
      },
      ambient: {
        intensity: 0
      },
      ambientCubemap: {
        texture: ROOT_PATH + '/data-gl/asset/canyon.hdr',
        exposure: 2,
        diffuseIntensity: 1,
        specularIntensity: 1
      }
    }
  },
  series: [
    {
      type: 'surface',
      parametric: true,
      wireframe: {
        show: false
      },
      shading: 'realistic',
      realisticMaterial: {
        roughness: 0.4,
        metalness: 0
      },
      parametricEquation: {
        u: {
          min: -Math.PI,
          max: Math.PI,
          step: Math.PI / 40
        },
        v: {
          min: -15,
          max: 6,
          step: 0.21
        },
        x: function (u, v) {
          return Math.pow(1.16, v) * Math.cos(v) * (1 + Math.cos(u));
        },
        y: function (u, v) {
          return -Math.pow(1.16, v) * Math.sin(v) * (1 + Math.cos(u));
        },
        z: function (u, v) {
          return -2 * Math.pow(1.16, v) * (1 + Math.sin(u));
        }
      }
    }
  ]
};
```

