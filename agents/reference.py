Llama8B_abdomen = """The diagnostic criteria are offered as a reference; however, it is essential to consider the actual condition of the patient comprehensively. Please provide a diagnosis that aligns with the patient's specific situation.
Cholecystitis general:
Gallbladder wall appearance is 'indistinct and hazy' suggesting chronic inflammation
No evidence of acute cholecystitis complications such as perforation, gangrene, or abscess formation
Right upper quadrant (RUQ) and epigastric pain
Presence of gallstones
Normal enhancement pattern of the liver and absence of intra-hepatic biliary obstruction suggest that this condition is not related to obstructive jaundice
Cholecystitis rare:
Circumferential wall edema up to 14mm
Questionable focal wall interruption at the gallbladder fundus
Adenomyomatosis (comet tail artifacts along the gallbladder wall)
Presence of multiple gallstones (>7)
Presence of a small subhepatic/pericholecystic fluid collection
Heterogeneous appearance and increased vascularity of the gallbladder wall

Appendicitis general:
Initial periumbilical abdominal pain that localizes to the Right Lower Quadrant (RLQ)
Some individuals experience general discomfort, fatigue, or lack of interest in food before experiencing more severe symptoms.
Change in Stool Consistency.
Nausea/Vomiting.
Imaging findings of a dilated appendix
Localized RLQ tenderness with rebound and involuntary guarding
Appendicitis rare:
Recurrent episodes of RLQ abdominal pain over an extended period
Cases might also feature secondary infections or co-morbidities affecting overall patient health
Blockage of the appendix can lead to its dilation and subsequent rupture
Pain migration patterns vary among individuals, sometimes beginning centrally before moving to the RLQ
Certain cases involve retrocecal positioning, increasing the likelihood of perforation

Pancreatitis general:
Elevated serum lipase level (>3 times the upper limit of normal)
Severe epigastric pain radiating to back, often worse after eating.
Presence of gallstone in the distal Common Bile Duct (CBD)
Recent increased consumption of alcohol
Markedly increased serum amylase/lipase levels indicative of pancreatic damage/enzyme leakage into bloodstream.
Pancreatitis rare:
Elevated lipase level
Change in stool pattern from tan and solid to dark and loose
Presence of diffuse dilation of the common bile duct with numerous filling defects on ERCP imaging

Diverticulitis general:
Imaging studies showing multiple diverticula in the distal thickened sigmoid colon
Increased white blood cell count indicative of systemic inflammatory response syndrome.
Presence of significant stranding around the sigmoid colon
Diverticulitis rare:
Thickening of the sigmoid colon wall (>50%)
Extraluminal air without organized collection, suggesting recent perforation
Partial or complete blockage of the intestines by swollen segments, causing severe vomiting, abdominal tenderness, and cessation of gas passage.
Loss of fat plane between the left ovary and the colon
"""



Llama8B_chest = """The diagnostic criteria are offered as a reference; however, it is essential to consider the actual condition of the patient comprehensively. Please provide a diagnosis that aligns with the patient's specific situation.
Pericarditis general:
Unilateral chest pain worsening with deep breathing and exertion
Electrocardiographic Changes: Specific electrocardiogram patterns like low voltage QRS complexes (<5mm), diffuse ST elevation without reciprocal changes, or PR interval prolongation.
A distinctive friction rub heard over the precordium during auscultation.
Elevated inflammatory markers (CRP > 10 mg/L)
Mild tortuosity of the thoracic aorta
Enlarged cardiac silhouette
Pericarditis rare:
Presence of pulsus paradoxus (> 10 mmHg)
Normal echocardiogram showing no evidence of cardiac tamponade or ventricular dysfunction
Positive family history of autoimmune diseases
Mild metabolic acidosis and elevated white blood cell count suggesting inflammation
Resolution of symptoms after drainage of the pericardial fluid
Recent history of trauma (bike accident)

Pneumonia general:
Respiratory Failure: Characterized by difficulty breathing, low oxygen saturation, and increased work of breathing, typically developing progressively.
Fever: Temperature exceeding 38°C was noted in most cases, often with associated chills.
Radiographic evidence of consolidation: Lobar or segmental consolidation visible on imaging.
Physical examination findings: Coarse breath sounds, absent or diminished breath sounds, and localized crackles were detected, especially over the site of consolidation.
Increased White Blood Cell Count: A hallmark sign of infection, often exceeding 12,000 cells/microL with neutrophilic predominance.
Altered Mental Status: Suggestive of systemic infection affecting brain function, particularly in older or severely ill patients.
Productive cough: Cough producing purulent sputum.
Pneumonia rare:
Presence of Infection Markers: Such as elevated CRP and procalcitonin, indicative of ongoing bacterial infection rather than thrombotic inflammation.
Patchy ill-defined opacity in the right lung base: Typically represents infection-related inflammation.
Mild leukopenia: Some patients, especially immunocompromised, showed a decrease in total white blood cell count.
Severe Hypoxemia: Extremely low oxygen saturation levels in the blood, necessitating urgent treatment.
Severe Bronchospasm: Can accompany pneumonia in patients with underlying reactive airway disease.
Presence of leukocytes in urine: Reflects systemic inflammatory response.
Patchy infiltration: Ground-glass patches and multifocal consolidation were visible on CT scans, suggestive of infectious.

Pulmonary Embolism general:
Sudden onset of shortness of breath
Risk Factors: History of recent surgery, immobility, and previous trauma to the hips.
Absence of signs of right heart strain on echocardiogram.
Recent history of deep vein thrombosis (DVT).
Underlying Condition: Presence of mixed connective tissue disease.
Elevated D-Dimer Levels: Extremely high d-dimer levels exceeding expected ranges.
Markedly low blood pressure requiring vasopressor support.
Pulmonary Embolism rare:
Markedly low blood pressure requiring vasopressor support.
Low molecular weight heparin therapy discontinued before symptom onset.
Low Platelet Count: Platelet count significantly below normal range.
Simple renal cysts
Echocardiographic evidence of increased RV pressure leading to dilatation.
Small Right Pleural Effusion: Presence of trace right pleural effusion.
Reflux of contrast within the IVC and hepatic veins.
"""


Deepseek_abdomen = """The diagnostic criteria are offered as a reference; however, it is essential to consider the actual condition of the patient comprehensively. Please provide a diagnosis that aligns with the patient's specific situation.
Cholecystitis general:
Positive sonographic Murphy's sign
Right upper quadrant (RUQ) pain, often severe and persistent
Elevated white blood cell count (leukocytosis)
Gallbladder wall thickening (>4mm) with pericholecystic fluid
Presence of gallstones on imaging
Mild elevation of liver enzymes (ALT/AST)
Cholecystitis rare:
Proteinuria without significant hematuria
Significantly elevated liver enzymes (ALT/AST) in the presence of choledocholithiasis
Pericholecystic fluid collection, sometimes indicating gallbladder perforation or evolving abscess
Layering sludge in the gallbladder without visible gallstones, seen in acalculous cholecystitis
Rim sign on CT 
Bile duct dilation with documented stones

Appendicitis general:
Right lower quadrant abdominal pain
Tenderness at McBurney's point
Elevated white blood cell count (ranging from 9.9 to 27.5 K/uL)
Appendiceal wall thickening and luminal distension observed on CT imaging
Nausea and vomiting
Periappendiceal fat stranding on imaging
Enlarged appendix (size varying from 6mm to over 1 cm)
Appendicitis rare:
Presence of appendicoliths on imaging
Free pelvic fluid without overt signs of perforation
Abscess formation or fluid collections
Reactive periappendiceal lymph nodes
Reactive terminal ileitis
Absence of free air ruling out perforation

Pancreatitis general:
Elevated Amylase/Lipase >3 times the upper limit of normal
Severe epigastric abdominal pain radiating to the back, often worsened by eating
Persistent nausea and vomiting, often leading to dehydration
Leukocytosis (elevated white blood cell count)
Abdominal tenderness upon physical examination, but no rebound tenderness unless complicated by necrosis or infection
Peripancreatic fluid collections and fat stranding with necrosis on CT
Pancreatitis rare:
Severe nausea and vomiting leading to profound dehydration and electrolyte imbalances
Biliary dilation or sludge without evidence of gallstone obstruction, suggesting biliary pancreatitis
Peripancreatic fat necrosis confirmed by imaging, often with pancreatic parenchymal changes
Unintentional weight loss (e.g., 30 lbs over three weeks) due to prolonged illness or exocrine insufficiency
Leukoysis (High WBC Count)
History of gallstone-related symptoms without acute cholecystitis features, but with signs of biliary pancreatitis

Diverticulitis general:
Left lower quadrant (LLQ) abdominal tenderness on physical examination
CT scan revealing diverticula and potential complications.  
Elevated white blood cell count
Absence of free air or diffuse peritoneal signs on initial imaging, suggesting contained inflammation rather than perforation
Clinical presentation includig abdominal pain, fever, constipation or diarrhea, and bloating
CT imaging shows colonic wall thickening (commonly >4 mm) in the sigmoid colon, with pericolic fat stranding
Diverticulitis rare:
Free air (pneumoperitoneum) on CT, indicating perforation
Dark-colored stools or gastrointestinal (GI) bleeding
Symptom improvement with antibiotics followed by relapse
Extensive diverticulosis of the colon observed on CT, without active inflammation
Widespread activation of immune cells throughout the body, potentially leading to shock, organ failure, or sepsis if left untreated.
Extraluminal gas localized to the left lower quadrant
"""



Deepseek_chest = """The diagnostic criteria are offered as a reference; however, it is essential to consider the actual condition of the patient comprehensively. Please provide a diagnosis that aligns with the patient's specific situation.
Pericarditis general:
Positional chest pain improving with sitting up and leaning forward
Elevated inflammatory markers (e.g., CRP, ESR, WBC)
Electrocardiogram showin ST elevations or prolonged PR intervals.  
Evidence of pericardial effusion on imaging studies (echocardiogram, CT, or radiography)
Positional chest pain improving when sitting up and leaning forward
Pericardial friction rub upon auscultation.
Pericarditis rare:
Signs of cardiac tamponade (distended neck veins, hypotension).  
High ESR with marked leukocyrosis (e.g., Neutrophils ≥75%)
Radiographic evidence of water-bottle-shaped heart

Pneumonia general:
Productive cough, often yellow, green, or blood-streaked sputum 
Low-grade to moderate fever (e.g., >100.4°F), commonly accompanied by chills and malaise
Shortness of breath that is progressive, typically gradual onset
Elevated white blood cell count with neutrophil predominance (neutrophilia), supporting infectious etiology
Ground-glass opacities or lobar/segmental consolidations on chest imaging (X-ray or CT)
Crackles (rales) or bronchial breath sounds heard on auscultation
Pneumonia rare:
Extensive lung consolidation involving multiple lobes, sometimes progressing to acute respiratory distress syndrome (ARDS)
Hypoxemia unresponsive to oxygen therapy, indicating severe pulmonary involvement
Weight loss, poor appetite, and night sweats, especially with chronic infections like tuberculosis or fungal pneumonia
Bibasilar atelectasis visible on imaging, secondary to obstruction or infection
Pleuritic chest pain that worsens with coughing or deep inspiration but does not improve with positional changes

Pulmonary Embolism general:
Filling defects in pulmonary arteries on CT angiography (e.g., main, segmental, or subsegmental branches)
Tachycardia (rapid heart rate), typically defined as > 100 bpm
Elevated D-dimer levels
Hypoxia (low oxygen saturation, e.g., SpO₂ < 90%)
Signs of right ventricular strain on echocardiography
Direct visualization of thrombi via CT pulmonary anglography.  
Sudden onset of dyspnea
Pulmonary Embolism rare:
Wedge-shaped opacity consistent with pulmonary infarct
Extremely elevated D-dimer levels (>5000 ng/mL)
Electrocardiogram abnormalities (e.g., ST segment depression, T wave inversion)
Bilateral saddle emboli causing extensive occlusion
Pro-BNP elevation (e.g., 1147 ng/mL)
Presentation with cough, fever, and tachypnea
Elevated Troponin and BNP levels indicating cardiac strain
"""



Llama70B_abdomen = """The diagnostic criteria are offered as a reference; however, it is essential to consider the actual condition of the patient comprehensively. Please provide a diagnosis that aligns with the patient's specific situation.
Cholecystitis general:
Right upper quadrant abdominal pain and tenderness
Presence of multiple risk factors such as previous episodes of tumor flare-ups, recent changes in diabetic regimen leading to hypoglycemia, and use of Sorafenib therapy increasing the risk of thromboembolic events and subsequent development of ascending cholangitis
Positive Sonographic Murphy's sign
Imaging findings of dilated common bile ducts and choledocholithiasis on ultrasound abdomen
Elevated white blood cell count
Fever >38°C (100.4°F)
Elevated Liver enzymes (ALT, AST)
Cholecystitis rare:
Perforation of the gallbladder with abscess formation
Ischemic Gallbladder Necrosis due to Arterial Occlusion secondary to Pseudoaneurysms
Ascending Cholangitis secondary to Choledochoolithiasis
Presence of sludge within the gallbladder
Gallbladder wall edema and minimal thickening (<3mm)
Absence of choelithiasis does not rule out acute cholecystitis

Appendicitis general:
Abdominal pain localized to the right lower quadrant
Elevated white blood cell count
Presence of nausea and vomiting
Presence of periappendiceal fat stranding
Imaging findings of a dilated appendix
Tenderness to palpation over the right lower quadrant
Clinical presentation of nausea, vomiting, and fever
Appendicitis rare:
Presence of an appendicolith on imaging
Trace periappendical stranding
Non-filling of the appendix with mucosa hyperenhancement and dilatation of the appendiceal tip
Migration of abdominal pain from the peri-umblical area to the right lower quadrant
Free fluid tracking along the right paracolic gutter on computed tomography scan
Fluid-filled and dilated appendix measuring up to 13 mm in diameter
Dilation of the appendiceal tip, walls of the proximal and mid appendix are indistinct with surrounding fat standing, and adjacent cecal tip thickening

Pancreatitis general:
Elevated serum lipase level (> 3 times upper limit of normal)
Nausea and vomiting
Imaging findings suggestive of pancreatitis (enlargement, necrosis, or inflammation)
Severe epigastric pain radiating to back, often worse after eating.
Elevated serum amylase level
Elevated white blood cell count indicating infection/inflammation.
Imaging evidence such as CT scan showing pancreatic inflammation/enlargement 
Pancreatitis rare:
History of recent heavy ethanol consumption,
Imaging showing a pancreatic mass with surrounding inflammation and necrosis,
Worsening symptoms despite previous treatment,
Presence of gallstones and a dilated common bile duct on ultrasound,
Splenic vein thrombosis,
Post-endoscopic retrograde cholangiopancreatography (ERCP)-induced pancreatitis indicated by recent ERCP procedure,
Elevated liver enzymes indicative of associated liver involvemen

Diverticulitis general:
Surrounding fat stranding
Leukocytosis (Elevated White Blood Cell Count)
Presence of colonic diverticulosis on imaging studies
Fever
Thickening of the sigmoid colon
Diverticulitis rare:
Contained perforation indicated by extraluminal air
Small foci of extraluminal air adjacent to the sigmoid colon
Notable involvement of the sigmoid mesocolon with surrounding fat stranding
Micro-abscess formation
Phlegmonous fluid collection interposed between the sigmoid colon and bladder
Pneumoperitoneum due to perforation of diverticula
"""



Llama70B_chest = """The diagnostic criteria are offered as a reference; however, it is essential to consider the actual condition of the patient comprehensively. Please provide a diagnosis that aligns with the patient's specific situation.
Pericarditis general:
Pleuritic chest pain that worsens with deep breathing
Elevated white blood cell count
Pericardial friction rub upon auscultation.  
Normal cardiac biomarkers (e.g., Troponin-T < 0.01 ng/mL)
Elevated inflammatory markers (such as CRP or ESR)
Widened mediastinum on portable chest radiograph
Pericarditis rare:
Positional variation in chest pain (improvement with leaning forward)
Uremic pericarditis due to end-stage renal disease (ESRD)
Low-grade fever (<101°F)
Bibasilar linear opacities consistent with discoid atelectasis and mild bronchial wall thickening on imaging studies
Presence of pericardial friction rub may be absent early in disease course
Radiation-free chest pain exacerbated by deep breathing and movement
Malignant pericarditis due to metastatic disease from non-Hodgkin's lymphoma (NHL)

Pneumonia general:
Clinical presentation consistent with respiratory infection (fever, cough, productive sputum).
Elevated white blood cell count
Radiographic evidence of new infiltrate(s), lobar or segmental pattern
Laboratory confirmation via Gram stain/culture of blood/sputum/tracheal aspirates or urinary antigen testing positive for Legionela pneumophilia or Streptococcus pneumoniae serotype
Patient's history of possible aspiration event with oral secretions.
Ground glass opacity in the right lower and middle lobe on CT scan indicating alveolar damage.
Pneumonia rare:
Recent history of dental procedure which may be considered as risk factor for aspiration pneumonia
Underlying condition of chronic lymphocytic leukemia (CLL) making patient susceptible to infections.
Bronchiectasis in the right lower lobe with peribronchial wall thickening.
Presence of risk factors for aspiration including history of recurrent aspirations, seizures, and recent enteral feeding tube placement.
Delirium secondary to pneumonia

Pulmonary Embolism general:
Sudden onset of dyspnea
Presence of risk factors such as recent surgery, immobility, and malignancy
Imaging findings of filling defects in the pulmonary arteries on CT scan
Elevated D-dimer level (>1000 ng/ml)
Pleuritic chest pain
Tachypnea
Pulmonary Embolism rare:
Extensive bilateral pulmonary emboli including a saddle embolus at the bifurcation of the main pulmonary artery
History of breast cancer with current radiation therapy and recent discontinuation of anticoagulation therapy
Heterozygosity for the prothrombin gene mutation indicating inherited thrombophilia
Wedge-shaped, peripheral-based consolidation consistent with pulmonary infarct
Near occlusive acute thrombus within the right main pulmonary artery with extension into the lobar, segmental and subsegmental branches of the right lung
Central filling defects in the right main, right middle, interlobar, and posterior basal segmental pulmonary arteries consistent with acute PE
"""