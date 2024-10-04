import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from google.generativeai.types import generation_types

# API 키 설정
GOOGLE_API_KEY = "AIzaSyC4fJPC5WpPcEAsKkhvU37xrBKcvv7XfwA"
genai.configure(api_key=GOOGLE_API_KEY)


def process_text(text):
    # Generation 설정
    generation_config = {
        "temperature": 0.5,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "application/json",
    }

    # Gemini 모델 설정
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        },
        system_instruction="""If I give you a prompt in Korean, describe the prompt in detail so you can draw well, make it good, and translate it into English.
        

Or, if you give me the plot of a novel, describe the prompt in detail so that I can draw the novel cover well based on the plot of the novel, and create a prompt like an example.

Please create a web novel cover with only one composition.

The example is {"prompt": "score_9, score_8_up, score_7_up, score_6_up, 1girl, alternate costume, alternate hairstyle, artist name, blonde hair, blue background, blush, butterfly-shaped pupils, chestnut mouth, cowboy shot, double bun, food, hair bun, hair ribbon, holding, holding ice cream cone, ice cream, ice cream cone, long sleeves, open mouth, pink pupils, pink ribbon, red bag, ribbon, shirt, simple background, solo, symbol-shaped pupils, too many, too many scoops, white shirt", "negative_prompt": "(low quality, worst quality:1.4), negativeXL_D, cgi,  text, signature, watermark, extra limbs"} ,

{"prompt": "(absurdres, highres, ultra detailed), 2others, couple, 1boy with 1girl, mature, (Height difference1.3), different hair color, happy, love, (hug), upper body, long hair girl, blonde and black hair, fantasy, russia, winter, knight and lady, closed mouth", "negative_prompt": "EasyNegative, (worst quality, low quality:1.4, blurry:1.4, badhandv4), multiple views, (aged down, teenage, blush)"}
{"prompt": "score_9, score_8_up, best quality. 4K, White lighting:1.2. masterpiece, high quality. 1girl, high resolution, Beautiful detailed eyes, black hair, long hair, ponytail hair, hair ribbon, red eyes, smile, blush, open mouth, eyelashes, tongue, school uniform, choker, simple background, thighhighs, thighs", "negative_prompt": "realistic, monochrome, greyscale, artist name, signature, watermark, ugly hands"} 
""",
    )

    # 텍스트를 기반으로 컨텐츠 생성
    try:
        response = model.generate_content([text])
        print("Full response: ", response)  # 전체 응답 확인
        if response.candidates:
            response_content = response.candidates[0].content.parts[0].text
            return response_content
        else:
            print("No candidates in the response.")
            return None
    except generation_types.StopCandidateException as e:
        print(e)
    except Exception as e:
        print(f"Error generating content: {str(e)}")
        return None


def main():
    input_text = input("Enter the story: ")  # 사용자 입력을 받음
    response_text = process_text(input_text)  # 입력된 텍스트 처리

    if response_text:
        print("Processing result:")
        print(response_text)  # 처리 결과 출력

if __name__ == "__main__":
    main()
