from django.db import models

# Create your models here.
class Website(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField(blank=True)
    screenshot = models.ImageField(upload_to='screenshots', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.screenshot:
            import chromedriver_binary
            from selenium import webdriver

            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('window-size=1200x600')
            driver = webdriver.Chrome(options=options)
            driver.get(self.url)
            image_path = 'screenshots/{}.png'.format(self.name)
            driver.save_screenshot(f"media/{image_path}")
            self.screenshot =  image_path
            driver.quit()
            


        return super(Website, self).save(*args, **kwargs)