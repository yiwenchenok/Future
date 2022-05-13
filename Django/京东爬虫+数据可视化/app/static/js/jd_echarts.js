var get_line_option = function (name, data_x, data_y) {
    return {
        tooltip: {
            trigger: 'axis'
        },
        toolbox: {
            feature: {
                dataZoom: {
                    yAxisIndex: "none"
                },
                dataView: {
                    readOnly: false
                },
                magicType: {
                    type: ['line', 'bar', 'stack']
                },
                restore: {},
            }
        },
        legend: {
            top: "0%",
            // left: "0%",
            textStyle: {
                color: "rgba(255,255,255,0.9)",
                fontSize: 12
            },
            data: [name]
        },
        grid: {
            center: '10',
            top: "30",
            right: '10',
            bottom: '10',
            containLabel: true
        },

        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: data_x,
            axisLabel: {
                color: "#4c9bfd",//文本颜色,
                fontSize: 8,
            }
        },
        yAxis: {
            type: 'value',
            name: '销量',
            axisLabel: {
                color: "#4c9bfd"//文本颜色
            },
            axisLine: {
                show: true//去除轴线
            },
            splitLine: {
                lineStyle: "#012f4a" //分割线颜色
            }
        },
        series: [
            {
                name: name,
                type: 'line',
                smooth: true,
                data: data_y
            },
        ]
    };
}

$(function () {
    $.get("/product_data/",
        function (data, status) {
            // 销量与价格的关系
            var char1 = data['price_sale']
            var price_list = char1[0]
            var sale_list = char1[1]
            var my_char1 = echarts.init(document.querySelector(".line1 .chart"));
            // var my_char2 = echarts.init(document.querySelector(".line2 .chart"));
            // var my_char3 = echarts.init(document.querySelector(".line3 .chart"));
            // var my_char4 = echarts.init(document.querySelector(".line4 .chart"));
            // var my_char5 = echarts.init(document.querySelector(".line5 .chart"));
            option1 = get_line_option('销量', price_list, sale_list)
            my_char1.setOption(option1);

            //   不同性别鞋的的销量柱状图
            var char2 = data['gender_sale_line']
            var gender_list = char2[0]
            var gender_sale_list = char2[1]

            var option2 = {
                color: ["#3398DB"],
                tooltip: {
                    trigger: "axis",
                    axisPointer: {
                        type: "line",
                        lineStyle: {
                            opacity: 0,
                        },
                    },
                },
                legend: {
                    data: ["直接访问", "背景"],
                    show: false,
                },
                grid: {
                    left: "0%",
                    right: "0%",
                    bottom: "5%",
                    top: "7%",
                    height: "85%",
                    containLabel: true,
                    z: 22,
                },
                xAxis: [
                    {
                        type: "category",
                        gridIndex: 0,
                        data: gender_list,
                        axisTick: {
                            alignWithLabel: true,
                        },
                        axisLine: {
                            lineStyle: {
                                color: "#0c3b71",
                            },
                        },
                        axisLabel: {
                            show: true,
                            fontSize: 12,
                            color: 'rgba(255,255,255,.6)',
                            rotate: 60
                        },
                    },
                ],
                yAxis: [
                    {
                        type: "value",
                        gridIndex: 0,
                        splitLine: {
                            show: false,
                        },
                        axisTick: {
                            show: false,
                        },
                        min: 0,
                        axisLine: {
                            lineStyle: {
                                color: "#0c3b71",
                            },
                        },
                        axisLabel: {
                            color: "rgb(170,170,170)",
                            formatter: "{value}",
                        },
                    },
                    {
                        type: "value",
                        gridIndex: 0,
                        min: 0,
                        splitNumber: 12,
                        splitLine: {
                            show: false,
                        },
                        axisLine: {
                            show: false,
                        },
                        axisTick: {
                            show: false,
                        },
                        axisLabel: {
                            show: false,
                        },
                        splitArea: {
                            show: true,
                            areaStyle: {
                                color: ["rgba(250,250,250,0.0)", "rgba(250,250,250,0.05)"],
                            },
                        },
                    },
                ],
                series: [
                    {
                        name: "销量",
                        type: "bar",
                        barWidth: "30%",
                        xAxisIndex: 0,
                        yAxisIndex: 0,
                        itemStyle: {
                            normal: {
                                barBorderRadius: 30,
                                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                                    {
                                        offset: 0,
                                        color: "#00feff",
                                    },
                                    {
                                        offset: 0.5,
                                        color: "#027eff",
                                    },
                                    {
                                        offset: 1,
                                        color: "#0286ff",
                                    },
                                ]),
                            },
                        },
                        data: gender_sale_list,
                        zlevel: 11,
                    },
                ],
            };
            var my_char2 = echarts.init(document.querySelector(".line2 .chart"));
            my_char2.setOption(option2)

            //    不同性别写鞋饼图占比
            var gen_sale_pie = data['gen_sale_pie']
            var my_char3 = echarts.init(document.querySelector(".line3 .chart"));
            var option3 = {
                title: {
                    // text: '各个性别销量占比',
                    left: 'center',


                },
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    orient: 'vertical',
                    left: 'left',
                    textStyle: {
                        color: '#efefef',
                    }
                },
                series: [
                    {
                        name: '性别',
                        type: 'pie',
                        radius: '50%',
                        data: gen_sale_pie,
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(39,109,238,0.5)'
                            }
                        }
                    }
                ]
            };
            my_char3.setOption(option3)

            // top 10 店铺
            var char4 = data['top10_shop_line']
            var top_shop_list = char4[0]
            var top_shop_sale = char4[1]
            var max_data = 100
            for (var i = 0; i < top_shop_sale.length; i++) {
                if (top_shop_sale[i] > max_data) {
                    max_data = top_shop_sale[i]
                }
            }
            var my_char4 = echarts.init(document.querySelector(".top10_shop .chart"));
            var option4 = {
                tooltip: {show: false},
                grid: {left: 10, top: 10, bottom: 20, right: 10, containLabel: true},
                xAxis: {
                    type: 'value',
                    boundaryGap: false,
                    max: max_data * 1.5, // Math.ceil(max / 4) * 5 || 10
                    axisLine: {show: true, lineStyle: {color: '#ccc'}},
                    axisTick: {show: false},
                    axisLabel: {color: '#999'},
                    splitLine: {lineStyle: {color: ['#CEEDFF'], type: [5, 8], dashOffset: 3}},
                },
                yAxis: {
                    type: 'category',
                    data: top_shop_list,
                    axisLine: {show: true, lineStyle: {color: '#ccc'}},
                    axisTick: {length: 3},
                    axisLabel: {fontSize: 14, color: '#ffffff', margin: 30, padding: 0},
                    inverse: true,
                },
                series: [
                    {
                        name: '数量',
                        type: 'bar',
                        showBackground: true,
                        backgroundStyle: {color: 'rgba(82, 168, 255, 0.1)', borderRadius: [0, 8, 8, 0]},
                        itemStyle: {
                            color: '#52A8FF',
                            normal: {
                                borderRadius: [0, 8, 8, 0],
                                color: function (params) {
                                    // 定义一个颜色集合
                                    let colorList = [
                                        '#52A8FF',
                                        '#00B389',
                                        '#FFA940',
                                        '#FF5A57',
                                        '#29EFC4',
                                        '#F8AEA4',
                                        '#FFC53D',
                                        '#009982',
                                        '#C099FC',
                                        '#F5855F',
                                    ];
                                    // 对每个bar显示一种颜色
                                    return colorList[params.dataIndex];
                                },
                            },
                        },
                        barMaxWidth: 16,
                        label: {show: true, position: 'insideRight', offset: [-5, 1], color: '#fff'},
                        data: top_shop_sale,
                    },
                ],
            };
            my_char4.setOption(option4)
            // top10 品牌
            var char5 = data['top10_pinpai_line']
            var top_pinpai_list = char5[0]
            var top_pinpai_sale = char5[1]
            var max_data2 = 100
            for (var i = 0; i < top_pinpai_sale.length; i++) {
                if (top_pinpai_sale[i] > max_data) {
                    max_data2 = top_pinpai_sale[i]
                }
            }
            var my_char5 = echarts.init(document.querySelector(".top10-pinpai .chart"));

            var option5 = {
                color: ["#3398DB"],
                tooltip: {
                    trigger: "axis",
                    axisPointer: {
                        type: "line",
                        lineStyle: {
                            opacity: 0,
                        },
                    },
                },
                legend: {
                    data: ["直接访问", "背景"],
                    show: false,
                },
                grid: {
                    left: "0%",
                    right: "0%",
                    bottom: "5%",
                    top: "7%",
                    height: "85%",
                    containLabel: true,
                    z: 22,
                },
                xAxis: [
                    {
                        type: "category",
                        gridIndex: 0,
                        data: top_pinpai_list,
                        axisTick: {
                            alignWithLabel: true,
                        },
                        axisLine: {
                            lineStyle: {
                                color: "#0c3b71",
                            },
                        },
                        axisLabel: {
                            show: true,
                            fontSize: 10,
                            color: 'rgb(255,255,255)',
                            rotate: 60
                        },
                    },
                ],
                yAxis: [
                    {
                        type: "value",
                        gridIndex: 0,
                        splitLine: {
                            show: false,
                        },
                        axisTick: {
                            show: false,
                        },
                        min: 0,
                        max: max_data2,
                        axisLine: {
                            lineStyle: {
                                color: "#0c3b71",
                            },
                        },
                        axisLabel: {
                            color: "rgb(170,170,170)",
                            formatter: "{value}",
                        },
                    },
                    {
                        type: "value",
                        gridIndex: 0,
                        min: 0,
                        max: max_data2,
                        splitNumber: 12,
                        splitLine: {
                            show: false,
                        },
                        axisLine: {
                            show: false,
                        },
                        axisTick: {
                            show: false,
                        },
                        axisLabel: {
                            show: false,
                        },
                        splitArea: {
                            show: true,
                            areaStyle: {
                                color: ["rgba(250,250,250,0.0)", "rgba(250,250,250,0.05)"],
                            },
                        },
                    },
                ],
                series: [
                    {
                        name: "销量",
                        type: "bar",
                        barWidth: "30%",
                        xAxisIndex: 0,
                        yAxisIndex: 0,
                        itemStyle: {
                            normal: {
                                barBorderRadius: 30,
                                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                                    {
                                        offset: 0,
                                        color: "#00feff",
                                    },
                                    {
                                        offset: 0.5,
                                        color: "#027eff",
                                    },
                                    {
                                        offset: 1,
                                        color: "#0286ff",
                                    },
                                ]),
                            },
                        },
                        data: top_pinpai_sale,
                        zlevel: 11,
                    },
                ],
            };
            my_char5.setOption(option5)
        });
})