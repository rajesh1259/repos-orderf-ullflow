import self as self
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('../driver/chromedriver')

driver.get("https://www.expedia.co.in/")
driver.maximize_window()
driver.find_element(By.XPATH, "//*[@id='wizardMainRegion']/div/div/div/div/ul/li[2]/a/span").click()
test = driver.find_element(By.CSS_SELECTOR, "body.uitk-no-outline:nth-child(2) div.app-layer-base--active div.uitk-grid.pageWhiteBackground div.uitk-cell.Storefront-Homepage div.uitk-cell div.uitk-spacing.SpacingContainer.inlineSpacingContainerUnset.uitk-spacing-padding-block-unset.uitk-spacing-padding-inline-unset:nth-child(3) div.uitk-spacing.StorefrontWizardRegionBEX.uitk-spacing-margin-blockend-unset.uitk-spacing-padding-blockend-unset div.uitk-layout-grid.uitk-layout-grid-columns-small-2.uitk-layout-grid-columns-large-12.uitk-spacing.wizardCard.SimpleContainer.uitk-spacing-padding-medium-inline-six.uitk-spacing-padding-medium-blockstart-twelve div.uitk-card.uitk-card-roundcorner-all.uitk-card-has-border.uitk-spacing.multiLobCard.uitk-spacing-padding-blockend-none.uitk-layout-grid-item.uitk-layout-grid-item-columnspan.uitk-layout-grid-item-columnspan-small-2.uitk-layout-grid-item-columnspan-large-12.uitk-card-has-primary-theme div.uitk-tabs-container div.uitk-tabs-content div.uitk-tabs-pane.active:nth-child(2) div.uitk-spacing.wizardOverHeroImage.uitk-spacing-padding-inline-six form.WizardFlightPWA div.uitk-tabs-container-experimental:nth-child(2) div.uitk-tabs-content div.uitk-tabs-pane.active:nth-child(1) div.uitk-layout-grid.uitk-layout-grid-gap-three.uitk-layout-grid-columns-small-4.uitk-layout-grid-columns-medium-6.uitk-layout-grid-columns-large-12.uitk-spacing.uitk-spacing-padding-block-three:nth-child(2) div.uitk-layout-grid-item.uitk-layout-grid-item-columnspan.uitk-layout-grid-item-columnspan-small-4.uitk-layout-grid-item-columnspan-medium-6.uitk-layout-grid-item-columnspan-large-8:nth-child(1) div.uitk-layout-grid.uitk-layout-grid-gap-three.uitk-layout-grid-columns-small-1.uitk-layout-grid-columns-medium-2.Location.locationWithSwap div.uitk-layout-grid-item.uitk-layout-grid-item-columnspan.uitk-layout-grid-item-columnspan-small-1.uitk-layout-grid-item-columnspan-medium-1:nth-child(1) div:nth-child(1) div.uitk-typeahead div:nth-child(1) div.uitk-field.has-floatedLabel-label.has-icon.has-no-placeholder:nth-child(2) > button.uitk-fake-input.uitk-form-field-trigger:nth-child(3)")
test.send_keys("Pune")
test.click()
driver.implicitly_wait(20)
