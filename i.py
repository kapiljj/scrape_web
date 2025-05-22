from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scrape_projects():
    
    chrome_options = Options()
    chrome_options.add_argument('--headless') 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        
        driver.get("https://rera.odisha.gov.in/projects/project-list")

        
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "project-card"))
        )

       
        projects = driver.find_elements(By.CLASS_NAME, "project-card")[:6]
        project_data = []

        for project in projects:
            try:
                
                project_name = project.find_element(By.CLASS_NAME, "card-title").text.strip()
                promoter_name = project.find_element(By.TAG_NAME, "small").text.replace("by ", "").strip()

                # Collects data
                project_data.append({
                    "Project Name": project_name,
                    "Promoter Name": promoter_name,
                    # Placeholders for additional data
                    "Rera Regd. No": "N/A (Update logic for detail page)",
                    "Promoter Address": "N/A (Update logic for detail page)",
                    "GST No": "N/A (Update logic for detail page)"
                })

            except Exception as e:
                print(f"Error scraping: {str(e)}")

        return project_data

    finally:
        driver.quit()

if __name__ == "__main__":
    projects = scrape_projects()
    if projects:
        print("\nScraped Projects:")
        for idx, project in enumerate(projects, 1):
            print(f"\nProject {idx}:")
            for key, value in project.items():
                print(f"{key}: {value}")
    else:
        print("No projects were scraped.")
