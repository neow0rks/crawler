const fs = require('fs');
const puppeteer = require('puppeteer');

const BASE_URL = "https://www.vieclamtot.com";

const crawler = async (url) => {
    const page = await browser.newPage();
    try {
        page.goto(BASE_URL + url, {
            // timeout: 2000,
        });

        await new Promise(r => setTimeout(r, 3000));
    
        const show_phone_number_btn = await page.$('.sc-ifAKCX ');
    
        if (!show_phone_number_btn) {
            console.log("No phone number or page not found");
            old_data.data = [...old_data.data.slice(0, pointer_index), ...old_data.data.slice(pointer_index + 1)]
            await page.close();
            return;
        }
        await new Promise(r => setTimeout(r, 2000));
        
        await page.evaluate(() => window.stop());
    
        await show_phone_number_btn.click();
    
        await new Promise(r => setTimeout(r, 1000));
    
        const phone_number = await page.$eval('.sc-ifAKCX', el => el.innerText);
    
        console.log("New phone number: " + phone_number);
    
        old_data.data[pointer_index].phone = phone_number;
    
        pointer_index++;
    
        await page.close();

    } catch (error) {
        console.log("Catch",error);
        old_data.data = [...old_data.data.slice(0, pointer_index), ...old_data.data.slice(pointer_index + 1)]
        await page.close();
    }
};

const main = async () => {
    if (!browser) {
        browser = await puppeteer.launch({
            headless: false,
            defaultViewport: null,
            //dumpio: true,
            args: ["--window-size=1024,1024"],
            ignoreDefaultArgs: ["--mute-audio"],
        });
    }

    if (index === urls.length) {
        return;
    }

    await crawler(urls[index]);
    index++;
    await main(index);
    if (index === urls.length) {
        // save data to file
        old_data.total = old_data.data.length;
        fs.writeFileSync(`../data/tp_hcm/${district}/new_data.json`, JSON.stringify(old_data));
        await browser.close();
    }
};

// read urls from file
const district = 'huyen-binh-chanh';
const urls = fs.readFileSync(`../crawled/list_url_job_${district}.txt`, 'utf8').split('\n');
let browser = null;
//read data from file
let old_data = fs.readFileSync(`../data/tp_hcm/${district}/data.json`, 'utf8');
old_data = JSON.parse(old_data);
let pointer_index = 0;
let index = 0;
main(index);
let progress = setInterval(() => {
    // show progress
    console.log(`Progress: ${index}/${urls.length}`);
    if (index === urls.length) {
        // save data to file
        clearInterval(progress);
    }
}, 60000);