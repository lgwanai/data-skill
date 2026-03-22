## 图表类型： (Breather)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 图片资源提示
该图表需要加载以下类型的图片资源：
https://echarts.apache.org/examples/data-gl/asset/canyon.hdr
请在生成代码时保留图片 URL 参数位置，并在最终输出时明确提示用户提供相应的图片资源 URL。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
var sin = Math.sin;
var cos = Math.cos;
var pow = Math.pow;
var sqrt = Math.sqrt;
var cosh = Math.cosh;
var sinh = Math.sinh;
var PI = Math.PI;
var aa = 0.4;
var r = 1 - aa * aa;
var w = sqrt(r);
option = {
  toolbox: {
    left: 20,
    iconStyle: {
      normal: {
        borderColor: '#000'
      }
    },
    feature: {
      myExportObj: {
        title: 'Export OBJ',
        icon: 'M4.7,22.9L29.3,45.5L54.7,23.4M4.6,43.6L4.6,58L53.8,58L53.8,43.6M29.2,45.1L29.2,0',
        onclick: function () {
          var res = echarts.exportGL2PLY(myChart, {
            mainType: 'grid3D',
            index: 0
          });
          download(res, 'surface.ply', 'text/plain');
        }
      }
    }
  },
  tooltip: {},
  visualMap: {
    show: false,
    dimension: 2,
    min: -3,
    max: 3,
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
      enable: true,
      SSAO: {
        enable: true,
        radius: 4
      }
    },
    viewControl: {
      distance: 130,
      beta: 50
    },
    light: {
      main: {
        intensity: 2,
        shadow: true
      },
      ambient: {
        intensity: 0
      },
      ambientCubemap: {
        texture: ROOT_PATH + '/data-gl/asset/canyon.hdr',
        exposure: 2,
        diffuseIntensity: 0.2,
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
        roughness: 0.3,
        metalness: 0
      },
      parametricEquation: {
        u: {
          min: -13.2,
          max: 13.2,
          step: 0.2
        },
        v: {
          min: -37.4,
          max: 37.4,
          step: 0.2
        },
        x: function (u, v) {
          var denom = aa * (pow(w * cosh(aa * u), 2) + aa * pow(sin(w * v), 2));
          return -u + (2 * r * cosh(aa * u) * sinh(aa * u)) / denom;
        },
        y: function (u, v) {
          var denom = aa * (pow(w * cosh(aa * u), 2) + aa * pow(sin(w * v), 2));
          return (
            (2 *
              w *
              cosh(aa * u) *
              (-(w * cos(v) * cos(w * v)) - sin(v) * sin(w * v))) /
            denom
          );
        },
        z: function (u, v) {
          var denom = aa * (pow(w * cosh(aa * u), 2) + aa * pow(sin(w * v), 2));
          return (
            (2 *
              w *
              cosh(aa * u) *
              (-(w * sin(v) * cos(w * v)) + cos(v) * sin(w * v))) /
            denom
          );
        }
      }
    }
  ]
};
```

