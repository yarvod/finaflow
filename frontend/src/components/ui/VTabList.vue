<template>
    <div
        class="tab-list"
        :class="{
            '_new': isNewDesign,
            '_alternative-new':isAlternativeNewDesign
        }"
    >
        <div ref="wrapper" class="tab-list__wrap">
            <div class="tab-list__container">
                <div
                    v-for="(tab, index) in tabs"
                    :key="index"
                    ref="tab"
                    :class="[{
                        '_active': tab.value === value,
                        'tab': defaultLook,
                        'p1': !defaultLook,
                        '_disabled': tab.disabled,
                        '_tooltip': tab.tooltip && tab.disabled
                    }]"
                    :style="{display: tab.value === 'invest_project' ? 'none' : false}"
                    class="tab-list__tab"
                    @click="$emit('click-tab', tab.value)"
                >
                    <component
                        :is="tab.icon"
                        v-if="tab.icon"
                        class="tab__icon"
                        :style="{color: tab.iconColor}"
                    />

                    {{ tab.name }}

                    <div
                        v-if="tab.tooltip && tab.disabled"
                        :data-tooltip="tab.tooltip"
                        class="tab-list__tab-tooltip"
                    >
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'VTabList',

    props: {
        defaultLook: {
            type: Boolean,
            default: true,
        },

        isNewDesign: {
            type: Boolean,
            default: false,
        },

        isAlternativeNewDesign: {
            type: Boolean,
            default: false,
        },

        isScrollOnClickAvailable: {
            type: Boolean,
            default: false,
        },

        tabs: {
            type: Array,
            default: () => [],
        },

        value: {
            type: [String, Number],
            default: null,
        },

        dataLayerParam: {
            type: Object,
            default: () => ({}),
        },
    },

    watch: {
        value(value) {
            if (!this.isScrollOnClickAvailable) {
                return;
            }

            const currentTab = this.$refs.tab[this.tabs.findIndex(t => t.value === value)];

            this.$refs.wrapper.scrollTo({ left: currentTab.getBoundingClientRect().left - 16, behavior: 'smooth' });
        },
    },

};
</script>

<style lang="scss">
    .tab-list {
        &__wrap {
            overflow-x: auto;
            width: 100%;
            scrollbar-width: none;
            -ms-overflow-style: -ms-autohiding-scrollbar;

            &::-webkit-scrollbar {
                display: none;
            }
        }

        &__container {
            box-sizing: border-box;
            display: flex;

            @include respond-to(mobile) {
                width: 100%;
                padding: 0 16px;
            }
        }

        &__tab._disabled {
            color: $Base400;
            pointer-events: none;
            cursor: not-allowed;
        }

        &__tab._disabled._tooltip {
            &:hover {
                border: 1px solid $Gray200;
                background-color: $white;
                color: $Base400;
            }
        }

        &__tab:not(.tab) {
            position: relative;
            box-sizing: border-box;
            margin-left: -1px;
            padding: 12px 16px;
            border: 1px solid $Gray200;
            background-color: $white;
            text-align: center;
            transition: all .3s ease;
            cursor: pointer;
            user-select: none;

            @include respond-to(mobile) {
                flex-grow: 1;
                padding: 8px 16px;
            }

            &:first-child {
                margin-left: 0;
                border-radius: 8px 0 0 8px;
            }

            &:last-child {
                border-radius: 0 8px 8px 0;
            }

            &:hover {
                @include respond-to(desktop) {
                    border-color: $Base0;
                    background-color: $Base;
                    color: $Base1;
                }
            }

            &._active {
                z-index: 1;
                border-color: $Base1;
                background-color: $Base;
                color: $white;
            }
        }

        &__tab-tooltip {
            position: absolute;
            width: 100%;
            height: 100%;
            pointer-events: all;

            &:hover:before {
                opacity: 1;
            }

            &:before {
                content: attr(data-tooltip);
                position: absolute;
                bottom: 58px;
                left: 50%;
                box-sizing: border-box;
                width: 284px;
                padding: 12px 16px;
                border-radius: 8px;
                background: rgba(67, 73, 90, .9);
                backdrop-filter: blur(6px);
                text-align: center;
                font-size: 14px;
                font-weight: normal;
                line-height: 18px;
                color: $white;
                opacity: 0;
                pointer-events: none;
                transform: translateX(-50%);
                transition: opacity .3s ease;
            }

            @include respond-to(mobile) {
                display: none;
            }
        }

        &._new {
            .tab-list__wrap {
                //overflow: auto;
                display: block;
                overflow-x: auto;
                white-space: nowrap;
            }

            .tab-list__container {
                border-radius: 8px;
                border: 1px solid $Base300;

                @include respond-to(mobile) {
                    padding: 0;
                }
            }

            .tab-list__tab {
                display: flex;
                align-items: center;
                justify-content: center;
                flex-grow: 1;
                margin: -1px 0;
                padding: 16px 32px;
                border-radius: 8px;
                border: 1px solid transparent;
                background-color: transparent;
                line-height: 1;
                transition: all .3s ease;
                cursor: pointer;

                &:first-child {
                    margin-left: -1px;
                }

                &:last-child {
                    margin-right: -1px;
                }

                &:hover {
                    z-index: 1;
                    border-color: $Base0;
                    background-color: $Base0;
                    color: $white;
                }

                &._active {
                    z-index: 1;
                    border-color: $Base1;
                    background-color: $Base1;
                    color: $white;
                }

                &:after {
                    content: none;
                }

                &:not(:first-child) {
                    &:before {
                        content: '';
                        position: absolute;
                        top: 50%;
                        left: -2px;
                        width: 1px;
                        height: 16px;
                        background-color: $Base300;
                        transform: translateY(-50%);
                        transition: opacity .3s ease;

                        @include respond-to(mobile) {
                            height: 12px;
                        }
                    }

                    &:hover:before {
                        opacity: 0;
                    }
                }

                &._active:before,
                &._active ~ &:before {
                    opacity: 0;
                }
            }
        }

        &._alternative-new {
            .tab-list__container {
                padding: 4px;
                border-radius: 8px;
                background-color: $Base200;
            }

            .tab-list__tab {
                display: flex;
                align-items: center;
                justify-content: center;
                flex-grow: 1;
                border-radius: 6px;
                border: none;
                background-color: $Base200;
                color: $Base700;

                &:not(:last-child) {
                    margin-right: 8px;
                }

                &:hover {
                    border: none;
                    background-color: #f6f8fc;
                }

                &._active {
                    border: none;
                    background-color: $white;
                    color: $Base900;
                }

                @include respond-to(mobile) {
                    padding: 8px;
                    font-size: 14px;
                    line-height: 1;
                }
            }
        }
    }
</style>
