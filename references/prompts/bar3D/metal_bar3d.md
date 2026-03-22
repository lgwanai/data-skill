## 图表类型：三维柱状图 - 金属质感 (Metal Bar3D)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 图片资源提示
该图表需要加载以下类型的图片资源：
https://echarts.apache.org/examples/data-gl/asset/pisa.hdr
请在生成代码时保留图片 URL 参数位置，并在最终输出时明确提示用户提供相应的图片资源 URL。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
$.getScript(CDN_PATH + 'simplex-noise@2.4.0/simplex-noise.js').done(
  function () {
    var noise = new SimplexNoise(Math.random);
    function generateData(theta, min, max) {
      var data = [];
      for (var i = 0; i <= 20; i++) {
        for (var j = 0; j <= 20; j++) {
          var value = noise.noise2D(i / 20, j / 20);
          valMax = Math.max(valMax, value);
          valMin = Math.min(valMin, value);
          data.push([i, j, value * 2 + 4]);
        }
      }
      return data;
    }
    var valMin = Infinity;
    var valMax = -Infinity;
    var data = generateData(2, -5, 5);
    myChart.setOption(
      (option = {
        tooltip: {},
        xAxis3D: {
          type: 'value'
        },
        yAxis3D: {
          type: 'value'
        },
        zAxis3D: {
          type: 'value',
          max: 10,
          min: 0
        },
        grid3D: {
          environment: '#000',
          axisPointer: {
            show: false
          },
          postEffect: {
            enable: true,
            SSAO: {
              enable: true,
              radius: 5
            }
          },
          light: {
            main: {
              intensity: 3
            },
            ambientCubemap: {
              texture: ROOT_PATH + '/data-gl/asset/pisa.hdr',
              exposure: 1,
              diffuseIntensity: 0.5,
              specularIntensity: 2
            }
          }
        },
        series: [
          {
            type: 'bar3D',
            data: data,
            barSize: 4,
            bevelSize: 0.4,
            bevelSmoothness: 4,
            shading: 'realistic',
            realisticMaterial: {
              roughness: 0.3,
              metalness: 1
            },
            label: {
              textStyle: {
                fontSize: 16,
                borderWidth: 1
              }
            },
            itemStyle: {
              color: '#ccc'
            },
            emphasis: {
              label: {
                show: false
              }
            }
          }
        ]
      })
    );
  }
);
```

