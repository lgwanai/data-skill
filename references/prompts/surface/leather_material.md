## 图表类型：皮革材质 (Leather Material)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 图片资源提示
该图表需要加载以下类型的图片资源：
https://echarts.apache.org/examples/data-gl/asset/leather/leather_height.jpg
https://echarts.apache.org/examples/data-gl/asset/pisa.hdr
https://echarts.apache.org/examples/data-gl/asset/leather/leather_roughness.jpg
https://echarts.apache.org/examples/data-gl/asset/leather/leather_normal.jpg
请在生成代码时保留图片 URL 参数位置，并在最终输出时明确提示用户提供相应的图片资源 URL。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
var TILING = [4, 2];
var heightImg = new Image();
heightImg.onload = update;
heightImg.crossOrigin = 'anonymous';
heightImg.src = ROOT_PATH + '/data-gl/asset/leather/leather_height.jpg';
function update() {
  var canvas = document.createElement('canvas');
  var ctx = canvas.getContext('2d');
  var width = (canvas.width = heightImg.width);
  var height = (canvas.height = heightImg.height);
  ctx.drawImage(heightImg, 0, 0, width, height);
  var imgData = ctx.getImageData(0, 0, width, height).data;
  function getScale(u, v) {
    u = ((u / Math.PI) * 0.5 + 0.5) * TILING[0];
    v = (v / Math.PI) * TILING[1];
    u = Math.floor((u - Math.floor(u)) * (width - 1));
    v = Math.floor((1 - v + Math.floor(v)) * (height - 1));
    var idx = v * width + u;
    return 1 + imgData[idx * 4] / 255 / 20;
  }
  myChart.setOption({
    xAxis3D: {
      type: 'value',
      min: -1.5,
      max: 1.5
    },
    yAxis3D: {
      type: 'value',
      min: -1.5,
      max: 1.5
    },
    zAxis3D: {
      type: 'value',
      min: -1.5,
      max: 1.5
    },
    grid3D: {
      show: false,
      environment: 'none',
      axisPointer: {
        show: false
      },
      postEffect: {
        enable: true,
        screenSpaceAmbientOcclusion: {
          enable: true,
          radius: 10,
          intensity: 2,
          quality: 'high'
        },
        screenSpaceReflection: {
          enable: false
        },
        depthOfField: {
          enable: false,
          focalRange: 10,
          fstop: 4
        }
      },
      temporalSuperSampling: {
        enable: true
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
          texture: ROOT_PATH + '/data-gl/asset/pisa.hdr',
          exposure: 1,
          diffuseIntensity: 1,
          specularIntensity: 2
        }
      },
      viewControl: {
        distance: 80
        // projection: 'orthographic'
      }
    },
    series: [
      {
        type: 'surface',
        parametric: true,
        shading: 'realistic',
        silent: true,
        wireframe: {
          show: false
        },
        realisticMaterial: {
          // detailTexture: 'asset/leather/leather_albedo.jpg',
          roughness: ROOT_PATH + '/data-gl/asset/leather/leather_roughness.jpg',
          normalTexture:
            ROOT_PATH + '/data-gl/asset/leather/leather_normal.jpg',
          textureTiling: TILING
        },
        itemStyle: {
          color: '#300'
        },
        parametricEquation: {
          u: {
            min: -Math.PI,
            max: Math.PI,
            step: Math.PI / 100
          },
          v: {
            min: 0.4,
            max: Math.PI - 0.4,
            step: Math.PI / 100
          },
          x: function (u, v) {
            return Math.sin(v) * Math.sin(u) * getScale(u, v);
          },
          y: function (u, v) {
            return Math.sin(v) * Math.cos(u) * getScale(u, v);
          },
          z: function (u, v) {
            return Math.cos(v) * getScale(u, v);
          }
        }
      }
    ]
  });
}
```

