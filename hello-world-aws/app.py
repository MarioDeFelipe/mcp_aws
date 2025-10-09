#!/usr/bin/env python3
"""
Simple Hello World AWS Lambda Function
"""

import json
import datetime
from typing import Dict, Any

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    AWS Lambda handler for Hello World application
    """
    
    # Get current timestamp
    current_time = datetime.datetime.now().isoformat()
    
    # Get request information
    request_method = event.get('requestContext', {}).get('http', {}).get('method', 'UNKNOWN')
    source_ip = event.get('requestContext', {}).get('http', {}).get('sourceIp', 'unknown')
    user_agent = event.get('headers', {}).get('user-agent', 'unknown')
    
    # Create HTML response with dark theme and company branding
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello World - AWS Lambda</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #0a0a0a;
                color: #e0e0e0;
                min-height: 100vh;
                background-image: 
                    radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.1) 0%, transparent 50%),
                    radial-gradient(circle at 40% 40%, rgba(120, 255, 119, 0.05) 0%, transparent 50%);
                background-attachment: fixed;
            }}
            
            .container {{
                max-width: 1000px;
                margin: 0 auto;
                padding: 20px;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }}
            
            .header {{
                text-align: center;
                margin-bottom: 40px;
            }}
            
            .logo {{
                width: 120px;
                height: 120px;
                margin: 0 auto 20px;
                background: #1a1a1a;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                border: 2px solid #ff77c6;
                box-shadow: 
                    0 0 20px rgba(255, 119, 198, 0.3),
                    inset 0 0 20px rgba(120, 255, 119, 0.1);
                position: relative;
                overflow: hidden;
            }}
            
            .logo::before {{
                content: '';
                position: absolute;
                top: -50%;
                left: -50%;
                width: 200%;
                height: 200%;
                background: conic-gradient(
                    from 0deg,
                    transparent,
                    rgba(255, 119, 198, 0.1),
                    transparent,
                    rgba(120, 255, 119, 0.1),
                    transparent
                );
                animation: rotate 8s linear infinite;
            }}
            
            .alien-head {{
                width: 60px;
                height: 80px;
                background: #2a2a2a;
                border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
                position: relative;
                z-index: 1;
            }}
            
            .alien-eye {{
                position: absolute;
                width: 18px;
                height: 12px;
                background: #78ff77;
                border-radius: 50%;
                top: 35px;
                box-shadow: 
                    0 0 10px rgba(120, 255, 119, 0.8),
                    inset 0 0 5px rgba(120, 255, 119, 0.3);
                animation: glow 2s ease-in-out infinite alternate;
            }}
            
            .alien-eye.left {{ left: 12px; }}
            .alien-eye.right {{ right: 12px; }}
            
            @keyframes rotate {{
                from {{ transform: rotate(0deg); }}
                to {{ transform: rotate(360deg); }}
            }}
            
            @keyframes glow {{
                from {{ 
                    box-shadow: 
                        0 0 10px rgba(120, 255, 119, 0.8),
                        inset 0 0 5px rgba(120, 255, 119, 0.3);
                }}
                to {{ 
                    box-shadow: 
                        0 0 20px rgba(120, 255, 119, 1),
                        inset 0 0 10px rgba(120, 255, 119, 0.5);
                }}
            }}
            
            h1 {{
                font-size: 3em;
                font-weight: 700;
                background: linear-gradient(135deg, #78ff77 0%, #ff77c6 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                margin-bottom: 10px;
                text-shadow: 0 0 30px rgba(120, 255, 119, 0.3);
            }}
            
            .subtitle {{
                font-size: 1.2em;
                color: #a0a0a0;
                margin-bottom: 40px;
            }}
            
            .info-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
                margin-bottom: 40px;
            }}
            
            .info-box {{
                background: rgba(26, 26, 26, 0.8);
                border: 1px solid rgba(120, 255, 119, 0.2);
                border-radius: 15px;
                padding: 25px;
                backdrop-filter: blur(10px);
                transition: all 0.3s ease;
                position: relative;
                overflow: hidden;
            }}
            
            .info-box::before {{
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(120, 255, 119, 0.1), transparent);
                transition: left 0.5s ease;
            }}
            
            .info-box:hover {{
                border-color: rgba(255, 119, 198, 0.4);
                box-shadow: 0 10px 30px rgba(120, 255, 119, 0.1);
                transform: translateY(-5px);
            }}
            
            .info-box:hover::before {{
                left: 100%;
            }}
            
            .info-box h2 {{
                color: #78ff77;
                font-size: 1.4em;
                margin-bottom: 15px;
                display: flex;
                align-items: center;
                gap: 10px;
            }}
            
            .info-box p {{
                color: #c0c0c0;
                line-height: 1.6;
                margin-bottom: 10px;
            }}
            
            .info-box strong {{
                color: #ff77c6;
            }}
            
            .tech-stack {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
                margin-top: 20px;
            }}
            
            .tech-item {{
                background: rgba(120, 255, 119, 0.05);
                border: 1px solid rgba(120, 255, 119, 0.2);
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                transition: all 0.3s ease;
            }}
            
            .tech-item:hover {{
                background: rgba(255, 119, 198, 0.05);
                border-color: rgba(255, 119, 198, 0.3);
                transform: scale(1.05);
            }}
            
            .tech-item strong {{
                color: #78ff77;
                display: block;
                margin-bottom: 8px;
                font-size: 1.1em;
            }}
            
            .checklist {{
                list-style: none;
                padding: 0;
            }}
            
            .checklist li {{
                padding: 8px 0;
                position: relative;
                padding-left: 30px;
                color: #c0c0c0;
            }}
            
            .checklist li::before {{
                content: '✅';
                position: absolute;
                left: 0;
                color: #78ff77;
            }}
            
            .checklist li.pending::before {{
                content: '🔄';
                color: #ff77c6;
            }}
            
            .footer {{
                text-align: center;
                margin-top: 50px;
                padding: 30px;
                background: rgba(26, 26, 26, 0.5);
                border-radius: 15px;
                border: 1px solid rgba(120, 255, 119, 0.1);
            }}
            
            .footer p {{
                color: #a0a0a0;
                margin: 10px 0;
            }}
            
            .status-badge {{
                display: inline-block;
                padding: 5px 15px;
                background: rgba(120, 255, 119, 0.2);
                color: #78ff77;
                border-radius: 20px;
                font-size: 0.9em;
                border: 1px solid rgba(120, 255, 119, 0.3);
                margin-left: 10px;
            }}
            
            @media (max-width: 768px) {{
                .container {{
                    padding: 15px;
                }}
                
                h1 {{
                    font-size: 2.2em;
                }}
                
                .info-grid {{
                    grid-template-columns: 1fr;
                }}
                
                .tech-stack {{
                    grid-template-columns: 1fr;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="logo">
                    <div class="alien-head">
                        <div class="alien-eye left"></div>
                        <div class="alien-eye right"></div>
                    </div>
                </div>
                <h1>Hello World from AWS</h1>
                <p class="subtitle">Serverless Application • Live & Running<span class="status-badge">ONLINE</span></p>
            </div>
            
            <div class="info-grid">
                <div class="info-box">
                    <h2>👋 Welcome</h2>
                    <p>This is a serverless web application running on <strong>AWS Lambda</strong> with a public Function URL.</p>
                    <p>You're successfully accessing a cloud-native application deployed on Amazon Web Services!</p>
                </div>
                
                <div class="info-box">
                    <h2>📊 Request Information</h2>
                    <p><strong>Timestamp:</strong> {current_time}</p>
                    <p><strong>Method:</strong> {request_method}</p>
                    <p><strong>Your IP:</strong> {source_ip}</p>
                    <p><strong>User Agent:</strong> {user_agent[:80]}...</p>
                </div>
                
                <div class="info-box">
                    <h2>🛠️ Technology Stack</h2>
                    <div class="tech-stack">
                        <div class="tech-item">
                            <strong>⚡ AWS Lambda</strong>
                            Serverless Compute
                        </div>
                        <div class="tech-item">
                            <strong>🐍 Python 3.13</strong>
                            Runtime Environment
                        </div>
                        <div class="tech-item">
                            <strong>🌐 Function URL</strong>
                            Public Access
                        </div>
                        <div class="tech-item">
                            <strong>🎨 Dark UI</strong>
                            Modern Design
                        </div>
                    </div>
                </div>
                
                <div class="info-box">
                    <h2>🎯 Development Status</h2>
                    <p>Foundation for the <strong>SAP Datasphere Control Panel</strong></p>
                    <ul class="checklist">
                        <li>AWS Lambda deployment working</li>
                        <li>Public access configured</li>
                        <li>Python runtime ready</li>
                        <li>Dark theme implemented</li>
                        <li class="pending">FastAPI integration</li>
                        <li class="pending">React frontend</li>
                        <li class="pending">Database integration</li>
                        <li class="pending">Datasphere API connection</li>
                    </ul>
                </div>
            </div>
            
            <div class="footer">
                <p>🛸 Built with alien technology for <strong>SAP Datasphere → AWS Integration</strong></p>
                <p>Ready to build amazing things in the cloud! 🚀</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
            'Cache-Control': 'no-cache'
        },
        'body': html_content
    }

# For local testing
if __name__ == "__main__":
    # Test event
    test_event = {
        'requestContext': {
            'http': {
                'method': 'GET',
                'sourceIp': '127.0.0.1'
            }
        },
        'headers': {
            'user-agent': 'Test Browser'
        }
    }
    
    result = lambda_handler(test_event, None)
    print("Status Code:", result['statusCode'])
    print("Content Type:", result['headers']['Content-Type'])
    print("Body length:", len(result['body']))