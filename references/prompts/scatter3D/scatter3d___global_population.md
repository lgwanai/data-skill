## 图表类型：三维散点图 - 全球人口分布 (Scatter3D - Global Population)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data-gl/asset/data/population.json]**:
```json
数据是一个数组 (Array)，共 38654 项。单项结构示例：
[
  [
    -83,
    76.5,
    1.1
  ],
  [
    -85.5,
    73.5,
    2.9
  ]
]
```

### 图片资源提示
该图表需要加载以下类型的图片资源：
https://echarts.apache.org/examples/data-gl/asset/starfield.jpg
https://echarts.apache.org/examples/data-gl/asset/bathymetry_bw_composite_4k.jpg
https://echarts.apache.org/examples/data-gl/asset/lake.hdr
请在生成代码时保留图片 URL 参数位置，并在最终输出时明确提示用户提供相应的图片资源 URL。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
$.getJSON(ROOT_PATH + '/data-gl/asset/data/population.json', function (data) {
  data = data
    .filter(function (dataItem) {
      return dataItem[2] > 0;
    })
    .map(function (dataItem) {
      return [dataItem[0], dataItem[1], Math.sqrt(dataItem[2])];
    });
  myChart.setOption({
    visualMap: {
      show: false,
      min: 0,
      max: 60,
      inRange: {
        symbolSize: [1.0, 10.0]
      }
    },
    globe: {
      environment: ROOT_PATH + '/data-gl/asset/starfield.jpg',
      heightTexture:
        ROOT_PATH + '/data-gl/asset/bathymetry_bw_composite_4k.jpg',
      displacementScale: 0.05,
      displacementQuality: 'high',
      globeOuterRadius: 100,
      baseColor: '#000',
      shading: 'realistic',
      realisticMaterial: {
        roughness: 0.2,
        metalness: 0
      },
      postEffect: {
        enable: true,
        depthOfField: {
          focalRange: 15,
          enable: true,
          focalDistance: 100
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
          intensity: 0.1,
          shadow: false
        },
        ambientCubemap: {
          texture: ROOT_PATH + '/data-gl/asset/lake.hdr',
          exposure: 1,
          diffuseIntensity: 0.5,
          specularIntensity: 2
        }
      },
      viewControl: {
        autoRotate: false,
        beta: 180,
        alpha: 20,
        distance: 100
      }
    },
    series: {
      type: 'scatter3D',
      coordinateSystem: 'globe',
      blendMode: 'lighter',
      symbolSize: 2,
      itemStyle: {
        color: 'rgb(50, 50, 150)',
        opacity: 1
      },
      data: data
    }
  });
});
```

