def agent_cards_html():
    return f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>AI Agents</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        margin: 0;
                        padding: 20px;
                    }}
                    .card {{
                        background-color: #fff;
                        border-radius: 8px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                        margin: 20px 0;
                        padding: 20px;
                        max-width: 400px;
                    }}
                    .card h2 {{
                        margin-top: 0;
                        color: #333;
                    }}
                    .card p {{
                        color: #666;
                    }}
                    .card ul {{
                        list-style-type: disc;
                        padding-left: 20px;
                        color: #333;
                    }}
                </style>
            </head>
            <body>
                <div class="card">
                    <h2>Cyber security expert</h2>
                    <p><strong>Goal:</strong>Your Goal is to create more engagement in a pharma company, to get more associates to participate and raise awareness</p>
                    <p><strong>Backstory:</strong> You are a Cyber Security expert, with about 10-12 years of experience in Information Security, Compliance and Risk Management areas with a CISM certification</p>
                    <h3>Tasks:</h3>
                    <ul>
                        <li>Threats research</li>
                        <li>For indoor</li>
                        <li>For outdoor</li>
                    </ul>
                </div>

                <div class="card">
                    <h2>Creative lead</h2>
                    <p><strong>Goal:</strong> Your job is to refer to the top 10 threats and risks prepared by the cybersecurity expert, examine them and suggest the best suitable formats/ media to effectively convey the message and bring in the required awareness on cyber security among the associates</p>
                    <p><strong>Backstory:</strong> Beta was developed to enhance customer service by providing instant responses to customer queries and solving common issues.</p>
                    <h3>Tasks:</h3>
                    <ul>
                        <li>create detailed plan</li>
                        <li>create board game</li>
                        <li>create communication plan</li>
                        <li>create marketing tech</li>
                    </ul>
                </div>

                <div class="card">
                    <h2>Content writer</h2>
                    <p><strong>Goal:</strong> Your goal is to engage people, by writing stimulating content in english</p>
                    <p><strong>Backstory:</strong> You are a content Writer, with 8-12 years of experience in Content creation, creative writing, copy writing and communications</p>
                    <h3>Tasks:</h3>
                    <ul>
                        <li>create creative writing</li>
                    </ul>
                </div>

                <div class="card">
                    <h2>Graphic designer</h2>
                    <p><strong>Goal:</strong> Your job is to design the projects as received from the creative head and the related content as received from the content writer</p>
                    <p><strong>Backstory:</strong> You are a graphic designer, with at least 8 years of experience in design layout, illustration, drawing, writing, UI/UX, 2D and 3D animation</p>
                    <h3>Tasks:</h3>
                    <ul>
                        <li>create designs</li>
                    </ul>
                </div>

            </body>
            </html>
"""


def agent_cards_gallery_view_html():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI Agents</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 20px;
            }}
            .gallery {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
            }}
            .card {{
                background-color: #fff;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                padding: 20px;
                display: flex;
                flex-direction: column;
            }}
            .card h2 {{
                margin-top: 0;
                color: #333;
            }}
            .card p {{
                color: #666;
            }}
            .card ul {{
                list-style-type: disc;
                padding-left: 20px;
                color: #333;
            }}
        </style>
    </head>
    <body>
        <div class="gallery">
            <div class="card">
                <h2>Cyber security expert</h2>
                <p><strong>Goal:</strong> Your goal is to create more engagement in a pharma company, to get more associates to participate and raise awareness.</p>
                <p><strong>Backstory:</strong> You are a Cyber Security expert, with about 10-12 years of experience in Information Security, Compliance and Risk Management areas with a CISM certification.</p>
                <h3>Tasks:</h3>
                <ul>
                    <li>Threats research</li>
                    <li>For indoor</li>
                    <li>For outdoor</li>
                </ul>
            </div>
            <div class="card">
                <h2>Creative lead</h2>
                <p><strong>Goal:</strong> Your job is to refer to the top 10 threats and risks prepared by the cybersecurity expert, examine them and suggest the best suitable formats/ media to effectively convey the message and bring in the required awareness on cyber security among the associates.</p>
                <p><strong>Backstory:</strong> Beta was developed to enhance customer service by providing instant responses to customer queries and solving common issues.</p>
                <h3>Tasks:</h3>
                <ul>
                    <li>Create detailed plan</li>
                    <li>Create board game</li>
                    <li>Create communication plan</li>
                    <li>Create marketing tech</li>
                </ul>
            </div>
            <div class="card">
                <h2>Content writer</h2>
                <p><strong>Goal:</strong> Your goal is to engage people, by writing stimulating content in English.</p>
                <p><strong>Backstory:</strong> You are a content writer, with 8-12 years of experience in content creation, creative writing, copywriting, and communications.</p>
                <h3>Tasks:</h3>
                <ul>
                    <li>Create creative writing</li>
                </ul>
            </div>
            <div class="card">
                <h2>Graphic designer</h2>
                <p><strong>Goal:</strong> Your job is to design the projects as received from the creative head and the related content as received from the content writer.</p>
                <p><strong>Backstory:</strong> You are a graphic designer, with at least 8 years of experience in design layout, illustration, drawing, writing, UI/UX, 2D and 3D animation.</p>
                <h3>Tasks:</h3>
                <ul>
                    <li>Create designs</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """