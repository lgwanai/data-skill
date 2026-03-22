## 图表类型：Bar3D - 星云 (Bar3D - Myth)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 图片资源提示
该图表需要加载以下类型的图片资源：
https://echarts.apache.org/examples/data-gl/asset/starfield.jpg
https://echarts.apache.org/examples/data-gl/asset/canyon.hdr
https://echarts.apache.org/examples/data-gl/asset/sample.jpg
请在生成代码时保留图片 URL 参数位置，并在最终输出时明确提示用户提供相应的图片资源 URL。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
var img = new Image();
var canvas = document.createElement('canvas');
var ctx = canvas.getContext('2d');
img.onload = function () {
  var width = (canvas.width = img.width);
  var height = (canvas.height = img.height);
  ctx.drawImage(img, 0, 0, width, height);
  var imgData = ctx.getImageData(0, 0, width, height);
  var data = new Float32Array((imgData.data.length / 4) * 3);
  var off = 0;
  for (var i = 0; i < imgData.data.length / 4; i++) {
    var r = imgData.data[i * 4];
    var g = imgData.data[i * 4 + 1];
    var b = imgData.data[i * 4 + 2];
    var lum = 0.2125 * r + 0.7154 * g + 0.0721 * b;
    lum = (lum - 125) / 4 + 50;
    data[off++] = i % width;
    data[off++] = height - Math.floor(i / width);
    data[off++] = lum;
  }
  myChart.setOption(
    (option = {
      tooltip: {},
      backgroundColor: '#fff',
      xAxis3D: {
        type: 'value'
      },
      yAxis3D: {
        type: 'value'
      },
      zAxis3D: {
        type: 'value',
        min: 0,
        max: 100
      },
      grid3D: {
        show: false,
        viewControl: {
          alpha: 70,
          beta: 0
        },
        postEffect: {
          enable: true,
          depthOfField: {
            enable: true,
            blurRadius: 4,
            fstop: 10
          }
          // SSAO: {
          //     enable: true
          // }
        },
        boxDepth: 100,
        boxHeight: 20,
        environment: ROOT_PATH + '/data-gl/asset/starfield.jpg',
        light: {
          main: {
            shadow: true,
            intensity: 2
          },
          ambientCubemap: {
            texture: ROOT_PATH + '/data-gl/asset/canyon.hdr',
            exposure: 2,
            diffuseIntensity: 0.2
          }
        }
      },
      series: [
        {
          type: 'bar3D',
          shading: 'lambert',
          barSize: 0.8,
          silent: true,
          dimensions: ['x', 'y', 'z'],
          itemStyle: {
            color: function (params) {
              var i = params.dataIndex;
              var r = imgData.data[i * 4] / 255;
              var g = imgData.data[i * 4 + 1] / 255;
              var b = imgData.data[i * 4 + 2] / 255;
              var lum = 0.2125 * r + 0.7154 * g + 0.0721 * b;
              r *= lum * 2;
              g *= lum * 2;
              b *= lum * 2;
              return [r, g, b, 1];
            }
          },
          data: data
        }
      ]
    })
  );
};
img.src = ROOT_PATH + '/data-gl/asset/sample.jpg';
img.crossOrigin = 'Anonymous';
```

