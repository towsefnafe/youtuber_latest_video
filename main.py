from selenium import webdriver
import webbrowser as wb

path = 'E://chromedriver.exe'

channel_list_file = open('channel_list.txt').read()
channel_list = channel_list_file.split('\n')

browser = webdriver.Chrome(path)

lis = []

for channel in channel_list:
	browser.get(channel + '/videos')
	created_at = browser.find_element_by_xpath('//*[@id="metadata-line"]/span[2]').text
	if 'hours ago' in created_at:
		channel_name = browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/app-header-layout/div/app-header/div[2]/div[2]/div/div[1]/div/div[1]/ytd-channel-name/div/div/yt-formatted-string').text
		latest_video = browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[1]/div[1]/div[1]/div[1]/h3/a')
		lis.append([channel_name, latest_video.text, latest_video.get_attribute('href')])

browser.close()

print('-' * 40)
print('\n')
for video in range(len(lis)):
	print(str(video) + ' : ' + lis[video][0] + ' - ' + lis[video][1])
print('\n')
print('-'*40)

n = int(input('Enter the index: '))

wb.open(lis[n][2])